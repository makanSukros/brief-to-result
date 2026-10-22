# Brief to Result

**Lebih sedikit menyusun prompt. Lebih banyak pekerjaan selesai.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [Lisensi MIT](LICENSE)

Skill agent dengan bahasa dasar Inggris untuk pengguna global: **80 workflow, tiga Outcome Packs, Project Profiles opsional, dan Repair Mode dengan lingkup terarah**. Sampaikan hasil yang dibutuhkan, gunakan konteks proyek yang kamu pilih, lalu revisi hanya bagian yang perlu.

> Secara default, skill langsung mengerjakan permintaan. Prompt baru dibuat ketika diminta. Menyiapkan konten tidak otomatis memberi izin untuk memublikasikannya.

## Mulai dari pekerjaan nyata

Setelah skill dipasang, minta kepada agent:

```text
Gunakan Brief to Result: Launch Kit.
Ubah catatan rilis ini menjadi satu email pelanggan dan dua postingan sosial.
Gunakan hanya fakta yang tersedia. Tulis dalam bahasa Indonesia.
Siapkan draf saja, jangan publikasikan.
```

```text
Gunakan Brief to Result dengan profil proyek .btr/profiles/northstar.json.
Jadikan ide fitur ini requirement, user flow, acceptance criteria,
dan tugas implementasi berurutan. Tandai keputusan yang belum selesai.
Jangan mulai coding.
```

```text
Gunakan Brief to Result: Repair Mode.
Ubah paragraf pembuka saja. Pertahankan semua fakta produk, paragraf lainnya,
dan CTA tanpa perubahan. Berikan draf lengkap setelah revisi.
```

Pada client yang mendukungnya, gunakan `$brief-to-result`. Cara pemanggilan dan lokasi instalasi berbeda antar-agent; repository ini tidak mengklaim sudah menguji semua client.

## Isi paket

| Fitur | Hasil | Panduan |
| --- | --- | --- |
| **Outcome Packs** | Paket hasil yang konsisten, memakai fakta bersama dan pemeriksaan penyelesaian | [Protokol pack](brief-to-result/references/outcome-packs.md) |
| **Project Profiles** | Preferensi proyek lokal yang dipilih pengguna, serta catatan fakta dengan sumber dan tanggal | [Panduan profil](brief-to-result/references/project-profiles.md) |
| **Repair Mode** | Revisi terarah dengan perlindungan teks dan bagian di luar lingkup | [Panduan revisi](brief-to-result/references/repair-mode.md) |
| **80 workflow** | Penulisan, pemahaman, strategi, penjualan, konten, produk, teknis, dan operasional | [Instruksi utama](brief-to-result/SKILL.md) |

Panduan teknis dan instruksi skill tetap menggunakan bahasa Inggris. README ini memberi jalur penggunaan dalam bahasa Indonesia; hasil kerja mengikuti bahasa yang diminta pengguna.

### Tiga Outcome Packs

| Pack | Hasil bawaan |
| --- | --- |
| [Launch Kit](brief-to-result/packs/launch-kit.md) | Pesan utama, email, postingan sosial, FAQ, checklist peluncuran, sumber dan hal yang belum jelas |
| [Idea to Build](brief-to-result/packs/idea-to-build.md) | Brief, user flow, acceptance criteria, tugas implementasi, keputusan terbuka |
| [Research to Content](brief-to-result/packs/research-to-content.md) | Peta sumber, ringkasan, angle, draf, catatan verifikasi |

Lingkup permintaan mengalahkan hasil bawaan. Permintaan satu email tidak otomatis menjadi satu kampanye. Sumber yang tidak bisa dibaca, harga yang belum diketahui, dan hasil yang terhambat akan dijelaskan, bukan dikarang. Pack dijalankan oleh agent, bukan oleh script Python.

### Profil proyek tanpa memori tersembunyi

Profil harus dipilih secara eksplisit. Skill tidak memindai proyek lain atau otomatis menyimpan preferensi dari percakapan. Instruksi tugas terbaru mengalahkan preferensi profil. Saat mengedit, bahasa sumber dipertahankan kecuali diminta diterjemahkan. Konten baru memakai bahasa Inggris jika tidak ada ketentuan bahasa lain.

Preferensi dan fakta produk disimpan terpisah. Fakta yang mudah berubah membutuhkan sumber dan tanggal tinjauan. Helper menyisihkan fakta kedaluwarsa, belum terverifikasi, atau tidak berlaku. Label `confirmed` dikelola pengguna, **bukan bukti bahwa script memverifikasi kebenarannya**. File tetap berada di lokasi lokal yang dipilih, tetapi isinya dapat dilihat model ketika kamu meminta agent membacanya. Jangan simpan kredensial atau data pribadi pelanggan.

### Revisi yang tidak merombak semuanya

Repair Mode menentukan target, bagian yang boleh diubah, fakta/teks yang harus dipertahankan, dan kriteria keberhasilan. Helper teks opsional memeriksa hash sumber, menjaga bagian yang tidak dipilih, menampilkan diff, dan hanya menulis ke **file baru**. Rencana lama, rentang bertumpuk/tidak valid, dan perubahan teks terkunci akan ditolak. Makna, akurasi fakta, dan kualitas bahasa tetap perlu diperiksa.

## Instalasi

Clone repository, lalu salin **seluruh** direktori `brief-to-result/` di dalamnya ke lokasi skill yang didukung agent. Jangan hanya menyalin `SKILL.md`.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
```

Untuk pemasangan pertama pada agent yang mendukung `~/.agents/skills/`:

```bash
mkdir -p ~/.agents/skills
cp -R brief-to-result ~/.agents/skills/
```

Gunakan lokasi sesuai dokumentasi client jika berbeda. Jika sudah terpasang, periksa/cadangkan versi lama sebelum menggantinya; jangan mencampurkan file versi lama dan baru sembarangan. Simpan profil proyek di luar direktori skill agar pembaruan skill tidak mengganti data proyek.

Workflow Markdown dapat diikuti tanpa Python. Helper baru `btr.py` membutuhkan **Python 3.10+**, hanya memakai standard library, dan tidak melakukan panggilan jaringan/model. Kamu tetap membutuhkan agent yang kompatibel dan akses modelnya sendiri. Ini bukan aplikasi chatbot mandiri atau layanan otomatisasi latar belakang.

## Helper lokal

Jalankan contoh berikut dari root repository hasil clone. Untuk versi terpasang, ganti awalan `brief-to-result/` dengan lokasi instalasi sebenarnya.

### Cari dan baca pack

```bash
python3 brief-to-result/scripts/btr.py packs list
python3 brief-to-result/scripts/btr.py packs show launch-kit
```

Perintah ini menampilkan instruksi, bukan menghasilkan konten. `--json` menampilkan metadata pack dalam format terstruktur.

### Buat profil proyek

```bash
python3 brief-to-result/scripts/btr.py profiles init northstar
# Edit .btr/profiles/northstar.json dengan preferensi dan fakta proyek yang didukung sumber.
python3 brief-to-result/scripts/btr.py profiles check .btr/profiles/northstar.json
python3 brief-to-result/scripts/btr.py profiles context .btr/profiles/northstar.json
```

Inisialisasi menolak menimpa profil yang sudah ada dan membuat file ignore lokal jika belum tersedia. File tidak dienkripsi; aturan ignore tidak melindungi file yang sudah terlanjur dilacak Git. Periksa `git status` sebelum commit. Tambahkan `--as-of YYYY-MM-DD` untuk pemeriksaan tanggal yang dapat diulang, atau `--strict` pada `profiles check` agar fakta yang disisihkan membuat pemeriksaan gagal. Lihat [template](brief-to-result/assets/profile.template.json) dan [aturan skema lengkap](brief-to-result/references/project-profiles.md).

### Preview dan terapkan revisi terarah

Contoh produk Northstar yang disertakan bersifat fiktif. Buat rencana untuk baris pertamanya:

```bash
mkdir -p .btr
python3 brief-to-result/scripts/btr.py repair plan examples/repair-before.txt \
  --allow 1:1 --keep "Try the demo." --output .btr/repair.json
```

Edit hanya nilai `replacement` di `.btr/repair.json`; pertahankan `\n` di ujungnya. Contoh: `Export your report without retyping it.\n`. Setelah itu:

```bash
python3 brief-to-result/scripts/btr.py repair preview examples/repair-before.txt --plan .btr/repair.json
python3 brief-to-result/scripts/btr.py repair apply examples/repair-before.txt \
  --plan .btr/repair.json --output .btr/revised.txt
```

Ulangi `--allow START:END` untuk beberapa rentang baris sumber yang terpisah, dan `--keep` untuk teks tambahan yang harus dipertahankan persis. Preview tidak menulis file; apply menolak tujuan yang sudah ada. Helper hanya mendukung teks UTF-8, bukan dokumen biner. Rencana menyimpan cuplikan sumber, jadi perlakukan sesuai kerahasiaan sumbernya. Batas lingkup adalah kontrak yang dapat ditinjau, bukan sandbox keamanan.

### Helper workflow dan teks yang sudah ada

```bash
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/text_metrics.py --help
```

| Kategori | ID | Contoh |
| --- | --- | --- |
| Penulisan | W01–W10 | Revisi, ringkas, jaga gaya, balasan |
| Pemahaman | U01–U10 | Jelaskan, rangkum, bandingkan, ajarkan |
| Ide dan strategi | I01–I10 | Validasi, positioning, prioritas, blindspot |
| Penjualan | M01–M10 | Penawaran, landing page, keberatan |
| Konten | C01–C10 | Postingan, naskah, carousel |
| Produk | P01–P10 | PRD, alur, izin, kriteria |
| Teknis | T01–T10 | Debugging, review, integrasi, rilis |
| Operasional | O01–O10 | SOP, keputusan, dukungan, pengumuman |

Setiap workflow berisi trigger, input, metode, bentuk hasil, pemeriksaan, dan contoh. Bahasa dasar Inggris tidak berarti otomatis mengasumsikan pasar AS, dolar, atau zona waktu tertentu.

## Pengujian dan batasan

```bash
python3 -m unittest discover -s tests -v
```

Tes otomatis memeriksa helper lokal, penanganan error, kesegaran fakta, batas revisi teks, integritas katalog, dan tautan dokumentasi lokal. [Contoh pengujian manual](examples/README.md) mencakup tiga pack, prioritas bahasa, dan revisi terarah. Contoh itu bukan hasil benchmark model yang sudah diukur. Lulus tes lokal tidak membuktikan perilaku identik di semua agent, kebenaran fakta, atau peningkatan performa penjualan/konten.

Kode keluar helper: `0` berhasil, `1` ada fakta yang disisihkan saat pemeriksaan profil strict, `2` input tidak valid atau gagal menulis. Helper lama `text_metrics.py` memakai `1` ketika batas panjang gagal dipenuhi. Sumber yang berubah setelah rencana revisi dibuat membutuhkan rencana baru; file asli tidak pernah ditimpa.

## Lisensi dan perubahan

[MIT](LICENSE), copyright (c) 2026 makanSukros. [Salinan lisensi](brief-to-result/LICENSE) ikut dalam pemasangan skill mandiri. Lihat [CHANGELOG.md](CHANGELOG.md) untuk perubahan versi sumber.
