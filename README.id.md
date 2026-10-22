# Brief to Result

**Lebih sedikit menyusun prompt. Lebih banyak pekerjaan selesai.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [Lisensi MIT](LICENSE)

**Ubah permintaan sehari-hari menjadi hasil yang bisa dipakai:** hook affiliate yang spesifik, copy jualan, balasan pelanggan, draf konten, tindak lanjut rapat, latihan belajar, atau brief fitur untuk tim.

BTR adalah skill reusable untuk agent AI yang kompatibel, bukan chatbot terpisah atau model baru. Di dalamnya ada **80 workflow, Hook Lab dengan 24 formula kreatif, tiga Outcome Packs, Project Profiles opsional, Repair Mode, dan dialog adaptif**. Ceritakan kebutuhanmu dengan bahasa biasa. Tidak perlu menghafal nama fitur atau nomor workflow.

[Cara pakai](#quick-start) · [Percakapan interaktif](#dialogue) · [Contoh per kategori](#use-cases) · [Fitur](#features) · [Instalasi](#installation) · [Pengujian](#tests)

## Tujuan dan manfaat

Tujuannya mengurangi usaha dari **“bantu saya mengerjakan ini”** sampai mendapat hasil yang berguna. BTR memandu agent memakai konteks yang relevan, menanyakan keputusan penting, menjaga fakta dan batasan, lalu mengerjakan permintaan. Bukan mengembalikannya sebagai prompt yang lebih panjang.

Kamu bisa memakai ulang profil proyek yang dipilih, menyiapkan beberapa draf dengan fakta yang konsisten, dan merevisi bagian tertentu tanpa merombak semuanya. Skill tidak menambahkan browsing, akses file, pembuatan gambar, memori permanen, atau izin publikasi. Kemampuan itu mengikuti aplikasi yang menjalankannya. Tetap periksa fakta dan komitmen penting; ini bukan jaminan jawaban sempurna, viral, atau peningkatan penjualan.

<a id="quick-start"></a>
## Cukup panggil @btr

Setelah skill dipasang dan dipilih pada aplikasi yang mendukungnya:

```text
@btr buatin 12 hook affiliate buat produk ini. Anglenya harus beda-beda.
```

```text
bantu balas pelanggan ini dengan tenang dan jelas dong @btr
```

```text
@btr perbaiki pembukanya aja. Bagian lainnya jangan diubah.
```

Tempelkan atau lampirkan bahan yang relevan. BTR seharusnya memakai konteks yang sudah ada, bukan memintamu menjelaskannya ulang. Kalau tugasnya belum diketahui, cukup bertanya singkat. Gunakan `@btr menu` hanya ketika ingin melihat pilihan.

**Mention bukan instalasi otomatis.** Pemilihan skill mengikuti aplikasi. Client dengan awalan dolar memakai `$btr`; instalasi nama panjang memakai `$brief-to-result`. Lihat [panduan pemanggilan](brief-to-result/references/invocation.md). Menyiapkan draf tidak otomatis memberi izin mengirim atau memublikasikannya.

<a id="dialogue"></a>
## Interaktif saat perlu, langsung mengerjakan saat sudah jelas

Percakapan bukan kuesioner wajib. BTR memeriksa apakah jawaban yang belum ada benar-benar akan mengubah hasil sebelum bertanya.

| Situasi | Perilaku yang diarahkan |
| --- | --- |
| Tugas dan bahannya sudah jelas. | Langsung kerjakan. |
| Jawabannya ada di lampiran atau percakapan sebelumnya. | Baca atau gunakan dulu, jangan tanya ulang. |
| Ada keputusan yang mengubah pendekatan. | Tanyakan satu hal paling menentukan, jelaskan alasannya bila membantu. |
| Permintaan bergantung pada klaim yang belum didukung. | Tunjukkan masalahnya dan gunakan alternatif yang jujur jika memungkinkan. |
| Kamu menjawab “belum tahu”. | Beri rekomendasi sementara atau dua arah konkret untuk dibandingkan. |
| Kamu mengoreksi jawaban sebelumnya. | Pakai koreksinya tanpa mengulang seluruh proses awal. |
| Kamu bilang “langsung buat, jangan tanya lagi”. | Hentikan pertanyaan opsional, bukan mengarang informasi penting. |
| Informasinya sudah cukup. | Berhenti mewawancarai dan berikan hasil. |

**Contoh: menyesuaikan konsep video produk.** Ini ilustrasi, bukan benchmark model independen.

> **Kamu:** Bantu konsep video penjepit kabel sesuai bahan visual yang bisa saya pakai. Saya belum jelaskan asetnya.
>
> **BTR:** Kamu punya rekaman produk dipakai, atau hanya foto produk? Ini menentukan apakah pembukanya bisa langsung menunjukkan demo.
>
> **Kamu:** Baru foto.
>
> **BTR:** Pakai pembuka berbasis foto, bukan pengujian palsu. Teks layar: “Ujung kabelnya di mana lagi?” Lanjutkan dengan foto produk dan fungsi penahan kabel yang sebenarnya.

Kalau kamu hanya meminta hook teks dan fungsi produknya sudah jelas, BTR seharusnya **tidak menanyakan rekaman demo**. Contoh pertanyaan yang berguna bukan berarti menjadi kolom wajib setiap tugas.

Cukup katakan `@btr bantu saya mikirin ini`, `@btr bongkar asumsi yang saya lewatkan`, atau `@btr langsung buat dari fakta yang ada`. Ini permintaan biasa, bukan perintah baru yang harus dihafal. Dalam diskusi terpandu, setelah dua putaran pertanyaan sebaiknya sudah ada draf, rangkuman, atau opsi konkret sebelum menggali lagi, kecuali kamu memang meminta wawancara lebih panjang. Sumber yang belum tersedia tetap bisa menghambat jawaban yang jujur. Lihat [aturan dialog adaptif](brief-to-result/references/adaptive-dialogue.md) dan [bukti serta batas pengujian](evals/README.md).

<a id="use-cases"></a>
## Pilih contoh sesuai pekerjaanmu

Pilih kategori, salin perintahnya, lalu sertakan bahan yang disebutkan. Contoh lanjutan memakai konteks sebelumnya. Kategori ini bukan mode yang perlu diatur.

| Kamu bekerja sebagai… | Langsung ke contoh | Hasil yang bisa diminta |
| --- | --- | --- |
| Affiliator | [Affiliator](#affiliates) | Hook, konsep demo, revisi pembuka |
| Seller atau pemilik UMKM | [Seller dan UMKM](#sellers) | Copy produk, balasan keberatan, draf peluncuran |
| Kreator atau pengelola media sosial | [Kreator](#creators) | Postingan, carousel, adaptasi konten |
| Marketer atau copywriter | [Marketing](#marketing) | Angle, landing page, rencana A/B |
| Freelancer atau agency | [Freelancer](#freelancers) | Proposal, komunikasi scope, revisi |
| Customer service atau admin | [CS dan Admin](#support) | Balasan, FAQ, eskalasi |
| Pekerja atau manajer tim | [Tim](#teams) | Tindak lanjut rapat, prioritas, SOP |
| Pelajar, mahasiswa, atau pengajar | [Belajar](#learning) | Penjelasan, latihan, rencana pelajaran |
| Founder, tim produk, atau developer | [Produk](#product) | Validasi, requirement, debugging |
| Pengguna untuk urusan pribadi | [Sehari-hari](#everyday) | Pesan, rencana, perbandingan |

<a id="affiliates"></a>
### Contoh pemakaian untuk Affiliator

**Bisa membantu:** mencari sudut jualan, membuat hook, menyusun konsep video, dan merevisi pembuka. **Bahan yang berguna:** fungsi produk, calon pengguna, visual yang tersedia, penawaran yang berlaku, dan pengalaman asli jika relevan. Tidak harus lengkap semua untuk mulai.

```text
@btr buatin 12 hook affiliate untuk penjepit kabel yang menahan ujung kabel
di tepi meja. Targetnya orang yang bekerja di meja. Bahasa Indonesia,
natural, sedikit nyindir, dan situasinya beda-beda, bukan ganti sinonim.
Jangan ngarang harga, popularitas, atau pengalaman pakai. Hooknya saja.
```

```text
@btr pilih tiga hook paling menarik dari tadi. Masing-masing jadiin
pembuka, adegan pertama, demo, dan satu CTA. Target sekitar 20 detik;
durasinya perkiraan sampai dibaca. Saya bisa dapat komisi affiliate,
jadi sertakan keterangan yang jelas dalam naskahnya.
```

```text
@btr pembukanya masih generik. Ubah hooknya saja dengan kejadian
sehari-hari yang lebih spesifik. Fakta produk, isi naskah, dan CTA tetap.
Jangan bikin testimoni palsu.
```

**Hasil yang dituju:** alasan memperhatikan produk yang berbeda dan demo yang menjawab hook. Untuk contoh fiktif penjepit kabel, kalimat “Alat kecil ini bikin hidup lebih mudah” bisa menjadi **“Mejanya udah estetik. Nyari kabelnya masih harus merangkak.”** Adegan berikutnya perlu menunjukkan masalah dan fungsi produk yang sebenarnya.

[Hook Lab](brief-to-result/references/hook-lab.md) memakai [24 formula](brief-to-result/references/hook-formulas.md), bukan sekadar mengganti nama barang dalam kalimat populer. [Contoh tambahan](brief-to-result/references/hook-examples.md) adalah ilustrasi, bukan bukti peningkatan conversion.

<a id="sellers"></a>
### Contoh pemakaian untuk Seller dan UMKM

**Bisa membantu:** menjelaskan manfaat, menjawab keberatan, dan membuat pesan peluncuran yang konsisten. **Bahan:** spesifikasi, harga dan syarat asli, target pembeli, atau pesan pelanggan.

```text
@btr tulis ulang deskripsi produk ini untuk pembeli pertama kali.
Jelaskan setiap fitur membantu masalah apa. Pertahankan spesifikasi,
harga, dan keterbatasan. Berikan deskripsinya, bukan tips menulis.
```

```text
@btr buat balasan singkat dan ramah untuk pelanggan yang bilang mahal.
Gunakan manfaat dan syarat yang saya berikan. Jangan mengarang diskon
atau menekan pelanggan supaya membeli.
```

```text
@btr dari catatan rilis dan penawaran yang sudah pasti ini, buat satu
email pelanggan, dua postingan sosial, dan lima jawaban FAQ.
Fakta produk harus konsisten. Siapkan draf, jangan publikasikan.
```

**Hasil yang dituju:** copy yang membantu pembeli memahami produk. Kebijakan yang belum diketahui tidak boleh berubah menjadi janji karangan.

<a id="creators"></a>
### Contoh pemakaian untuk Kreator dan Social Media

**Bisa membantu:** menemukan angle dan mengadaptasi konten dengan gaya yang konsisten. **Bahan:** artikel, transkrip, catatan, draf, atau contoh tulisanmu.

```text
@btr jadikan artikel ini dua postingan pendek untuk X dalam bahasa Inggris.
Buka dengan poin paling menarik yang didukung sumber. Pertahankan gaya
ngobrol saya dan batasan penting sumber. Isi harus memenuhi janji hook.
```

```text
@btr jadikan catatan ini carousel enam slide untuk pemula. Tiap slide
satu ide, teks singkat, dan arahan visual. Pembukanya harus spesifik,
bukan “Semua yang perlu kamu tahu”.
```

```text
@btr dari transkrip ini buat satu post LinkedIn, satu caption Instagram,
dan satu outline video pendek. Fakta tetap sama, angle dan struktur
sesuai kanal. Berikan draf, bukan jadwal posting.
```

**Hasil yang dituju:** draf sesuai kanal. Arahan visual bukan gambar yang sudah dibuat atau video yang sudah dirender.

<a id="marketing"></a>
### Contoh pemakaian untuk Marketing dan Copywriting

**Bisa membantu:** angle iklan, positioning yang jelas, dan hipotesis pengujian. **Bahan:** audiens, penawaran, bukti produk, landing page, serta batas kampanye.

```text
@btr buat lima angle iklan untuk penawaran dan audiens ini. Tiap angle
menjawab masalah, keraguan, atau motivasi membeli yang berbeda.
Berikan satu headline dan kalimat pembuka. Jangan pakai klaim tanpa bukti.
```

```text
@btr perbaiki bagian hero landing page ini saja. Perjelas untuk siapa,
apa manfaatnya, dan langkah berikutnya. Penawaran serta klaim asli tetap.
Berikan satu versi yang kamu rekomendasikan.
```

```text
@btr rancang A/B test untuk dua pembuka ini. Audiens, penawaran, isi,
dan CTA dibuat sebanding. Jelaskan hipotesis, ukuran hasil, dan batas
kesimpulannya. Jangan meramal CTR pemenang.
```

**Hasil yang dituju:** konsep berbeda dengan alasan yang bisa diuji, bukan skor performa buatan.

<a id="freelancers"></a>
### Contoh pemakaian untuk Freelancer dan Agency

**Bisa membantu:** scope yang jelas dan komunikasi klien yang profesional. **Bahan:** brief, hasil yang disepakati, biaya, waktu, serta aturan revisi.

```text
@btr jadikan brief klien ini proposal singkat: tujuan, hasil, batas scope,
dependensi, dan pertanyaan terbuka. Gunakan biaya dan waktu yang sudah
benar-benar disepakati. Tandai yang masih belum jelas.
```

```text
@btr bantu balas permintaan tambahan ini dengan ramah tetapi tegas.
Jelaskan bagian yang di luar scope terlampir dan apa yang perlu disepakati.
Jangan menjanjikan kerja gratis atau mengarang biaya baru.
```

```text
@btr terapkan feedback klien hanya pada headline dan paragraf penutup.
Isi yang sudah disetujui, fakta produk, dan deliverable jangan berubah.
Berikan hasil revisi dan ringkasan perubahannya.
```

**Hasil yang dituju:** proposal, balasan, atau revisi dengan batas jelas. Menulis draf tidak berarti mengirim atau menerima perjanjian.

<a id="support"></a>
### Contoh pemakaian untuk Customer Service dan Admin

**Bisa membantu:** balasan empatik, FAQ, dan catatan eskalasi. **Bahan:** pesan yang sudah disamarkan, kebijakan resmi, fakta insiden, atau catatan dukungan.

```text
@btr buat balasan tenang berdasarkan keluhan dan kebijakan layanan ini.
Akui masalahnya lalu jelaskan langkah berikutnya. Tanyakan hanya informasi
yang dibutuhkan. Jangan menjanjikan refund atau waktu selesai yang belum pasti.
```

```text
@btr kelompokkan pertanyaan pelanggan yang sudah disamarkan ini menjadi FAQ.
Jawab berdasarkan dokumentasi kami. Tandai pertanyaan yang belum terjawab,
jangan mengarang kebijakan.
```

```text
@btr jadikan percakapan ini catatan eskalasi: masalah, bukti, langkah yang
sudah dicoba, dampak, dan informasi yang masih dibutuhkan.
Pisahkan fakta dari dugaan penyebab.
```

**Hasil yang dituju:** draf dan catatan internal yang bisa ditinjau. Hilangkan data pribadi yang tidak diperlukan; tidak ada pengiriman otomatis.

<a id="teams"></a>
### Contoh pemakaian untuk Pekerja dan Manajer Tim

**Bisa membantu:** tindak lanjut rapat, prioritas realistis, dan prosedur berulang. **Bahan:** catatan, tenggat, kapasitas, atau deskripsi proses.

```text
@btr jadikan catatan rapat ini keputusan, tugas, penanggung jawab, dan tenggat.
Tandai nama atau tanggal yang belum disepakati. Pisahkan pertanyaan terbuka.
Jangan menambahkan komitmen yang tidak ada di catatan.
```

```text
@btr ini tugas dan tenggat saya. Waktu yang tersedia minggu ini enam jam.
Pilih tiga prioritas, apa yang ditunda, dan konsekuensinya.
Tandai perkiraan durasi. Jangan mengubah kalender.
```

```text
@btr jadikan proses ini SOP untuk anggota tim baru: kapan mulai,
bahan yang diperlukan, langkah, pengecualian, eskalasi, dan kriteria selesai.
Tandai keputusan kebijakan yang masih belum ada.
```

**Hasil yang dituju:** tindakan jelas tanpa mengarang keputusan atas nama orang lain.

<a id="learning"></a>
### Contoh pemakaian untuk Pelajar, Mahasiswa, dan Pengajar

**Bisa membantu:** pemahaman, latihan, dan rencana pembelajaran. **Bahan:** catatan, kutipan bab, tujuan belajar, tingkat peserta, atau jawaban yang sudah dicoba.

```text
@btr jelaskan bagian catatan ini untuk pemula. Mulai dari inti,
beri satu contoh konkret, lalu luruskan salah paham yang mungkin muncul.
Detail teknis harus tetap akurat.
```

```text
@btr buat lima soal dari catatan ini, dari mudah sampai lebih sulit.
Berikan soal dulu dan tunggu jawaban saya sebelum menjelaskan.
Tandai materi di luar catatan sebagai tambahan.
```

```text
@btr gunakan bahan ini untuk rencana pelajaran 30 menit sesuai tingkat peserta.
Masukkan tujuan, penjelasan, aktivitas, dan pemeriksaan pemahaman.
Durasi adalah rencana, bukan waktu yang sudah diukur.
```

**Hasil yang dituju:** penjelasan dan bahan belajar, bukan kutipan atau sumber palsu. Kuis interaktif boleh sengaja berhenti untuk menunggu jawabanmu.

<a id="product"></a>
### Contoh pemakaian untuk Founder, Product, dan Developer

**Bisa membantu:** menguji asumsi, memperjelas perilaku fitur, dan diagnosis berbasis bukti. **Bahan:** masalah, audiens, catatan fitur, alur, kode, log, atau langkah reproduksi.

```text
@btr tantang ide produk ini. Cari tiga asumsi paling berisiko,
bukti yang mendukung atau menolaknya, dan eksperimen kecil untuk mulai.
Jangan menganggap permintaan pasar sudah terbukti.
```

```text
@btr jadikan ide fitur ini brief, alur pengguna, acceptance criteria,
edge cases, dan tugas implementasi menurut dependensi.
Tandai keputusan yang belum selesai. Jangan coding dulu.
```

```text
@btr periksa error, kode terkait, dan langkah reproduksi ini.
Pisahkan observasi dari hipotesis. Sarankan pemeriksaan terkecil yang berguna,
lalu perbaikan terarah dan pengujiannya jika buktinya cukup.
```

**Hasil yang dituju:** rencana validasi, spesifikasi, atau diagnosis yang bisa ditindaklanjuti. Usulan perbaikan bukan perbaikan yang sudah diuji.

<a id="everyday"></a>
### Contoh pemakaian untuk Kebutuhan Sehari-hari

**Bisa membantu:** pesan yang jelas dan rencana praktis. **Bahan:** pesan, waktu, batasan, atau pilihan yang sedang dibandingkan.

```text
@btr bantu menolak undangan ini dengan ramah dan singkat.
Jangan mengarang alasan atau membuat janji untuk tanggal lain.
```

```text
@btr susun pekerjaan rumah ini menjadi rencana akhir pekan yang realistis.
Gunakan waktu dan batasan yang saya berikan. Tandai perkiraan dan jangan
menganggap orang lain sudah setuju membantu.
```

```text
@btr bandingkan pilihan ini sesuai prioritas saya. Rekomendasikan satu,
jelaskan konsekuensinya, dan informasi apa yang bisa mengubah keputusan.
Jangan menebak harga atau spesifikasi yang belum diketahui.
```

**Hasil yang dituju:** pesan atau rencana siap ditinjau. Tugas kecil tidak membutuhkan satu pack lengkap atau profil proyek.

<a id="features"></a>
## Isi paket

| Fitur | Kegunaan | Panduan |
| --- | --- | --- |
| Dialog adaptif | Pertanyaan penting, pemeriksaan blindspot, pemakaian jawaban, dan aturan berhenti | [Dialog](brief-to-result/references/adaptive-dialogue.md) |
| Hook Lab | Pembuka jualan dan affiliate dengan 24 formula kreatif | [Hook Lab](brief-to-result/references/hook-lab.md) |
| Outcome Packs | Beberapa hasil terkait dengan fakta sumber yang sama | [Packs](brief-to-result/references/outcome-packs.md) |
| Project Profiles | Preferensi lokal yang dipilih serta fakta dengan sumber dan tanggal | [Profil](brief-to-result/references/project-profiles.md) |
| Repair Mode | Revisi bagian tertentu sambil menjaga teks di sekitarnya | [Revisi](brief-to-result/references/repair-mode.md) |
| 80 workflow | Menulis, memahami, ide, penjualan, konten, produk, teknis, operasional | [SKILL.md](brief-to-result/SKILL.md) |

Tiga pack yang tersedia: [Launch Kit](brief-to-result/packs/launch-kit.md), [Idea to Build](brief-to-result/packs/idea-to-build.md), dan [Research to Content](brief-to-result/packs/research-to-content.md). Lingkup permintaan mengalahkan hasil bawaan. Satu email tidak otomatis menjadi kampanye; bagian yang terhambat tidak boleh diisi dengan karangan.

Profil bersifat lokal dan opt-in, bukan memori tersembunyi antar-chat. Label `confirmed` dikelola pengguna, bukan bukti verifikasi independen. Fakta kedaluwarsa, belum terverifikasi, atau tidak berlaku tidak boleh mengisi kekosongan copy. File tidak dienkripsi, dan profil yang dipilih bisa dibaca model. Jangan simpan kredensial atau data pribadi pelanggan.

Repair Mode membedakan usulan perubahan dengan perubahan yang benar-benar dikerjakan. Helper teks UTF-8 opsional memeriksa hash sumber dan teks terkunci, menampilkan diff, serta menulis hanya ke file baru. Helper tidak memverifikasi kebenaran isi atau mengedit dokumen biner.

Bahasa dasar dokumentasi tetap Inggris. Hasil mengikuti bahasa dan konteks yang diminta; teks yang diedit mempertahankan bahasanya kecuali diminta diterjemahkan. Bahasa Inggris tidak otomatis berarti pasar AS, dolar, atau zona waktu tertentu.

<a id="installation"></a>
## Instalasi

Sumber utama ada di `brief-to-result/`. Builder membuat paket skill mandiri bernama `btr`, lengkap dengan seluruh sumber runtime dan lisensi MIT.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
python3 tools/build_btr.py --output dist/btr.zip
```

Impor ZIP melalui alur unggah skill yang didukung aplikasi, tinjau, lalu aktifkan. Pemilihan `@` atau `$` mengikuti aplikasi; publikasi GitHub tidak memasangnya otomatis di akunmu. Lihat [panduan per aplikasi](brief-to-result/references/invocation.md).

Untuk pemasangan pertama pada client yang mendukung `~/.agents/skills/`:

```bash
python3 tools/build_btr.py --directory "$HOME/.agents/skills/btr"
```

Builder menolak lokasi yang sudah ada. Periksa/cadangkan instalasi lama sebelum menggantinya, simpan profil di luar folder skill, dan gunakan satu instalasi aktif. Nama panjang tetap didukung. Jangan hanya mengganti nama folder asli: nama direktori dan metadata harus cocok.

Instruksi Markdown bisa diikuti tanpa Python. Pembuatan paket dan helper baru membutuhkan **Python 3.10+**, hanya standard library, tanpa panggilan jaringan atau model. Kamu tetap membutuhkan agent yang kompatibel beserta akses modelnya. Ini bukan chatbot mandiri atau layanan latar belakang.

<a id="local-tools"></a>
## Alat bantu lokal opsional

Untuk penggunaan sehari-hari, cukup minta seperti biasa. Perintah berikut dijalankan dari root repository; sesuaikan lokasi jika memakai versi terpasang.

<details>
<summary><strong>Lihat pack dan workflow</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py packs list
python3 brief-to-result/scripts/btr.py packs show launch-kit
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/text_metrics.py --help
```

Perintah ini menampilkan instruksi atau menghitung teks, bukan membuat hasil dengan model. ID 80 workflow tetap W01-W10, U01-U10, I01-I10, M01-M10, C01-C10, P01-P10, T01-T10, dan O01-O10. Dua puluh empat formula H adalah resep kreatif tambahan, bukan workflow umum baru.

</details>

<details>
<summary><strong>Buat dan periksa profil proyek</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py profiles init northstar
# Edit .btr/profiles/northstar.json dengan preferensi dan fakta yang benar.
python3 brief-to-result/scripts/btr.py profiles check .btr/profiles/northstar.json
python3 brief-to-result/scripts/btr.py profiles context .btr/profiles/northstar.json
```

Inisialisasi menolak overwrite dan membuat file ignore jika belum ada. Aturan ignore tidak melindungi file yang sudah dilacak; periksa `git status`. Gunakan `--as-of YYYY-MM-DD` untuk memeriksa kesegaran fakta secara berulang, atau `--strict` agar fakta yang disisihkan membuat pemeriksaan gagal. Lihat [template](brief-to-result/assets/profile.template.json) dan [skema](brief-to-result/references/project-profiles.md).

</details>

<details>
<summary><strong>Preview revisi teks terarah</strong></summary>

Contoh Northstar bersifat fiktif.

```bash
mkdir -p .btr
python3 brief-to-result/scripts/btr.py repair plan examples/repair-before.txt \
  --allow 1:1 --keep "Try the demo." --output .btr/repair.json
```

Edit hanya nilai `replacement`, pertahankan `\n` di ujungnya. Contoh: `Export your report without retyping it.\n`. Lalu:

```bash
python3 brief-to-result/scripts/btr.py repair preview examples/repair-before.txt --plan .btr/repair.json
python3 brief-to-result/scripts/btr.py repair apply examples/repair-before.txt \
  --plan .btr/repair.json --output .btr/revised.txt
```

Preview tidak menulis file; apply menolak tujuan yang sudah ada. Ulangi `--allow START:END` untuk rentang baris asli yang terpisah dan `--keep` untuk teks terkunci. Rencana mengandung cuplikan sumber, jadi jaga kerahasiaannya. Ini kontrak lingkup yang bisa ditinjau, bukan sandbox keamanan.

</details>

<details>
<summary><strong>Periksa keputusan dialog</strong></summary>

```bash
python3 brief-to-result/scripts/dialogue_policy.py --state path/to/approved-local-state.json
```

Helper opsional ini membaca state terstruktur dan merekomendasikan langkah berikutnya. Ia tidak memahami percakapan mentah, menemukan blindspot sendiri, memverifikasi fakta, memanggil model, menulis file, atau memberi izin tindakan. Pengguna biasa tidak perlu membuat JSON. Lihat [kontrak state](brief-to-result/references/adaptive-dialogue.md).

</details>

<a id="tests"></a>
## Pengujian dan batasan

```bash
python3 -m unittest discover -s tests -v
```

Tes mencakup perilaku helper, kasus error, perpindahan keputusan dialog, pertanyaan berulang, jawaban belum tahu, koreksi, kemasan, integritas katalog, serta tautan lokal. [Delapan walkthrough percakapan](evals/dialogue-walkthroughs.json) berisi respons yang dibuat saat pengembangan dan pemeriksaan mekanis. Ini **tinjauan oleh pembuatnya sendiri, bukan eksekusi terpisah di aplikasi atau benchmark model independen**. Lihat [catatan evaluasi](evals/README.md) untuk perbedaan dan prosedur pengujian aplikasi nyata.

Lulus tes tidak membuktikan hasil identik di semua agent, ketepatan makna, kenaikan conversion, atau memori permanen. Penafsiran oleh model tetap berpengaruh. Kode keluar helper: `0` berhasil, `1` fakta disisihkan dalam pemeriksaan profil strict atau batas panjang teks gagal, `2` input tidak valid atau gagal menulis.

## Lisensi dan perubahan

[MIT](LICENSE), copyright (c) 2026 makanSukros. [Salinan lisensi](brief-to-result/LICENSE) ikut dalam paket mandiri. Lihat [CHANGELOG.md](CHANGELOG.md). Nomor versi menunjukkan perubahan sumber, bukan otomatis GitHub Release atau sertifikasi aplikasi.
