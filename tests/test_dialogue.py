"""Structured policy and packaging checks, NOT raw-language model evaluations."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "brief-to-result/scripts/dialogue_policy.py"
spec = importlib.util.spec_from_file_location("dialogue_policy", SCRIPT)
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


def gap(ident="audience", kind="leverage", **kw):
    item = dict(id=ident, kind=kind, question="Office users, travelers, or another audience?",
                changes="Changes the situation and vocabulary of the draft.", fallback="Compare two short angles.", lookup=False)
    item.update(kw)
    return item


class DialogueTests(unittest.TestCase):
    def action(self, state):
        return policy.next_action(state)["action"]

    def test_clear_task_executes(self):
        self.assertEqual(self.action({}), "do")

    def test_finished_task_stops(self):
        self.assertEqual(self.action({"complete": True}), "done")

    def test_missing_task_asks_once(self):
        state = {"task_known": False}
        self.assertEqual(self.action(state), "ask")
        state = policy.record_question(state, "__task__")
        self.assertEqual(self.action(state), "blocked")
        state = policy.record_answer(state, "__task__", "Rewrite this message.")
        self.assertEqual(self.action(state), "do")

    def test_missing_task_and_no_questions_does_not_invent_task(self):
        self.assertEqual(self.action({"mode": "draft", "task_known": False}), "blocked")

    def test_low_impact_preference_does_not_block(self):
        self.assertEqual(self.action({"gaps": [gap(kind="preference")]}), "draft")

    def test_question_without_a_consequence_is_skipped(self):
        self.assertEqual(self.action({"gaps": [gap(changes="")]}), "draft")

    def test_one_consequential_question_not_a_catalog(self):
        result = policy.next_action({"gaps": [gap(), gap("tone")]})
        self.assertEqual(result["action"], "ask")
        self.assertEqual(result["gap_id"], "audience")
        self.assertEqual(result["question"], gap()["question"])

    def test_answer_is_used_without_reasking(self):
        state = policy.record_question({"gaps": [gap()]}, "audience")
        state = policy.record_answer(state, "audience", "Office workers")
        self.assertEqual(self.action(state), "do")
        self.assertEqual(state["decisions"]["audience"]["value"], "Office workers")

    def test_volunteered_answer_does_not_require_prior_question(self):
        state = policy.record_answer({"gaps": [gap()]}, "audience", "Travelers")
        self.assertEqual(self.action(state), "do")

    def test_unsure_user_gets_a_first_pass(self):
        state = policy.record_answer({"gaps": [gap()]}, "audience", status="unknown")
        self.assertEqual(self.action(state), "draft")
        self.assertIsNone(policy.next_action(state)["question"])

    def test_deferred_question_is_not_repeated(self):
        state = policy.record_answer({"gaps": [gap()]}, "audience", status="deferred")
        self.assertEqual(self.action(state), "draft")

    def test_previously_asked_question_is_not_paraphrased_again(self):
        state = {"gaps": [gap(question="Which buyers should this target?")], "asked": ["audience"]}
        self.assertEqual(self.action(state), "draft")

    def test_correction_replaces_decision_not_other_state(self):
        state = policy.record_answer({"gaps": [gap(), gap("format")]}, "audience", "Office workers")
        state = policy.record_answer(state, "format", "Three hooks only")
        new = policy.record_answer(state, "audience", "Actually, travelers")
        self.assertEqual(new["decisions"]["audience"]["value"], "Actually, travelers")
        self.assertEqual(new["decisions"]["format"], state["decisions"]["format"])
        self.assertEqual(state["decisions"]["audience"]["value"], "Office workers")

    def test_two_question_rounds_trigger_progress(self):
        state = {"mode": "guided", "rounds_without_output": 2, "gaps": [gap()]}
        self.assertEqual(self.action(state), "draft")

    def test_guided_multiturn_sequence(self):
        state = {"mode": "guided", "gaps": [gap("audience"), gap("objective"), gap("voice")]}
        for ident, answer in [("audience", "Travelers"), ("objective", "Product fit")]:
            self.assertEqual(policy.next_action(state)["gap_id"], ident)
            state = policy.record_question(state, ident)
            state = policy.record_answer(state, ident, answer)
        self.assertEqual(self.action(state), "draft")
        state["rounds_without_output"] = 0  # Only after a real draft/synthesis was delivered.
        self.assertEqual(policy.next_action(state)["gap_id"], "voice")

    def test_no_questions_switch_is_respected(self):
        state = policy.record_question({"gaps": [gap(), gap("objective")]}, "audience")
        state["mode"] = "draft"
        self.assertEqual(self.action(state), "draft")

    def test_required_input_is_not_guessed_after_budget(self):
        self.assertEqual(self.action({"rounds_without_output": 3,
                                      "gaps": [gap("source", "blocker", fallback="")]}), "ask")

    def test_inspect_source_before_asking(self):
        state = {"gaps": [gap("price", "conflict", fallback="", lookup=True)]}
        self.assertEqual(self.action(state), "inspect")
        state["inspected"] = ["price"]
        self.assertEqual(self.action(state), "ask")

    def test_failed_lookup_and_unknown_answer_do_not_loop(self):
        state = {"gaps": [gap("source", "blocker", fallback="", lookup=True)], "inspected": ["source"]}
        state = policy.record_answer(state, "source", status="unknown")
        self.assertEqual(self.action(state), "blocked")

    def test_no_questions_still_allows_authorized_read(self):
        self.assertEqual(self.action({"mode": "draft", "gaps": [gap(lookup=True)]}), "inspect")

    def test_conflict_gets_one_priority_question(self):
        state = {"gaps": [gap(), gap("locked_length", "conflict", fallback="")]}
        self.assertEqual(policy.next_action(state)["gap_id"], "locked_length")

    def test_unsupported_claim_changes_approach(self):
        state = {"gaps": [gap("experience", "claim", fallback="Use a product-observation opening.")]}
        result = policy.next_action(state)
        self.assertEqual(result["action"], "challenge_and_draft")
        self.assertIsNone(result["question"])

    def test_mandatory_claim_without_evidence_is_not_silently_used(self):
        state = {"mode": "draft", "gaps": [gap("10x", "claim", fallback="")]}
        self.assertEqual(self.action(state), "blocked")

    def test_independent_outputs_are_not_all_blocked(self):
        state = {"mode": "draft", "partial_available": True,
                 "gaps": [gap("document", "blocker", fallback="")]}
        self.assertEqual(self.action(state), "partial")

    def test_false_completion_does_not_hide_a_required_input(self):
        self.assertNotEqual(self.action({"complete": True,
                                        "gaps": [gap("source", "blocker", fallback="")]}), "done")

    def test_invalid_states_are_rejected(self):
        invalid = [[], {"mode": "magic"}, {"mode": []}, {"task_known": "yes"},
                   {"rounds_without_output": True}, {"rounds_without_output": -1},
                   {"askedd": []}, {"gaps": {}}, {"asked": ["x", "x"]},
                   {"gaps": [gap(), gap()]}, {"gaps": [gap(lookup="yes")]},
                   {"gaps": [gap(kind="guess")]}, {"gaps": [gap(ident="__task__")]},
                   {"decisions": {"x": {"status": "answered", "value": ""}}}]
        for state in invalid:
            with self.subTest(state=state), self.assertRaises(ValueError):
                policy.next_action(state)

    def test_pure_decision_does_not_mutate_input(self):
        state = {"gaps": [gap()]}; before = copy.deepcopy(state)
        policy.next_action(state)
        self.assertEqual(state, before)

    def test_cannot_record_unselected_or_unknown_question(self):
        with self.assertRaises(ValueError):
            policy.record_question({"gaps": [gap()]}, "other")
        with self.assertRaises(ValueError):
            policy.record_answer({"gaps": [gap()]}, "other", "answer")

    def test_cli_no_write_and_unicode(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            state = {"gaps": [gap(question="Punya rekaman demo atau hanya foto produk?")]}
            path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
            before = path.read_bytes()
            out = subprocess.run([sys.executable, str(SCRIPT), "--state", str(path)],
                                 capture_output=True, text=True, timeout=10)
            self.assertEqual(out.returncode, 0, out.stderr)
            self.assertIn("rekaman", json.loads(out.stdout)["question"])
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(len(list(Path(tmp).iterdir())), 1)

    def test_cli_invalid_duplicate_or_oversize_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            for payload in ['{"mode":"auto","mode":"draft"}', '{', 'x' * (policy.MAX_BYTES + 1)]:
                path.write_text(payload)
                out = subprocess.run([sys.executable, str(SCRIPT), "--state", str(path)],
                                     capture_output=True, text=True, timeout=10)
                self.assertEqual(out.returncode, 2)
                self.assertNotIn("Traceback", out.stderr)

    def test_required_source_precedes_lower_priority_conflict(self):
        state = {"gaps": [gap("style", "conflict", fallback=""),
                          gap("source", "blocker", fallback="")]}
        self.assertEqual(policy.next_action(state)["gap_id"], "source")

    def test_packaged_policy_runs_from_installed_folder(self):
        spec = importlib.util.spec_from_file_location("dialogue_builder", ROOT / "tools/build_btr.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        with tempfile.TemporaryDirectory() as tmp:
            installed = Path(tmp) / "btr"
            builder.build(installed, directory=True)
            self.assertTrue((installed / "references/adaptive-dialogue.md").exists())
            state = Path(tmp) / "state.json"; state.write_text("{}")
            run = subprocess.run([sys.executable, str(installed / "scripts/dialogue_policy.py"),
                                  "--state", str(state)], cwd=tmp, capture_output=True,
                                 text=True, timeout=10)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["action"], "do")

    def test_runtime_contract_is_wired_without_old_blockers_only_rule(self):
        text = (ROOT / "brief-to-result/SKILL.md").read_text()
        self.assertIn("references/adaptive-dialogue.md", text)
        self.assertNotIn("Ask one focused question only when the missing answer prevents", text)
        self.assertIn("0.4.0", text)


if __name__ == "__main__":
    unittest.main()
