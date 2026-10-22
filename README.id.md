# Brief to Result

**Lebih sedikit menyusun prompt. Lebih banyak pekerjaan selesai.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [Lisensi MIT](LICENSE)

**Brief to Result membantu agent AI mengubah permintaan sehari-hari menjadi hasil yang bisa dipakai:** pesan yang siap diperiksa dan dikirim, catatan rapat yang rapi menjadi daftar tindakan, penjelasan materi yang lebih mudah dipahami, atau ide mentah yang menjadi rencana kerja.

Ceritakan kebutuhanmu dengan bahasa biasa, lalu sertakan teks, catatan, atau file yang relevan. Skill ini memandu agent yang kompatibel untuk memilih cara kerja, mengikuti batasan, dan memeriksa hasilnya. Kamu tidak perlu menghafal ID workflow atau menyusun prompt panjang untuk setiap tugas.

## Cukup panggil @btr

Setelah memasang paket **btr**, pilih skill-nya lalu ngobrol seperti biasa:

```text
tolong dong bantu saya @btr
```

```text
@btr bantu rapihin pesan ini, sopan tapi jangan kaku
```

```text
catatan rapat ini jadiin tugas yang jelas dong @btr
```

Mention boleh di awal, tengah, atau akhir permintaan. BTR memakai percakapan dan bahan yang relevan, lalu memilih cara kerja. Tidak perlu hafal nomor workflow, nama pack, atau perintah teknis untuk pemakaian sehari-hari. Kalau tugas dan konteksnya belum ada, cukup satu pertanyaan singkat, misalnya: **“Mau dibantu apa?”** Ketik `@btr menu` hanya saat ingin melihat beberapa pilihan.

**Di ChatGPT yang mendukung Skills:** ketik `@`, cari **BTR — Brief to Result**, lalu pilih skill yang sudah dipasang. **Di Codex CLI/IDE:** gunakan `$btr`. Teks mention saja tidak memasang skill atau menjamin pemilihan melalui menu. Ikuti [instalasi nama pendek](#instalasi) di bawah; instalasi nama panjang tetap didukung. Lihat [panduan pemanggilan](brief-to-result/references/invocation.md) untuk detail dan batasannya.

## Apa itu Brief to Result?

Ini adalah **kumpulan instruksi, contoh, dan alat bantu lokal opsional yang bisa dipakai ulang oleh agent AI**. Anggap sebagai panduan kerja untuk agent, bukan aplikasi chatbot terpisah atau model AI baru.

Di dalamnya ada **80 workflow, tiga Outcome Packs, Project Profiles opsional, dan Repair Mode dengan lingkup terarah**. Kamu bisa memakainya untuk pekerjaan kecil sehari-hari maupun proyek yang lebih besar, tanpa menjalankan seluruh katalog.

Kamu tetap membutuhkan agent yang kompatibel beserta akses modelnya. Membaca file, mencari sumber, membuat file hasil, dan tindakan lainnya bergantung pada alat serta izin yang tersedia pada agent tersebut. Skill tidak menambahkan kemampuan itu dengan sendirinya. Setelah terpasang, permintaan menulis dan menyusun rencana biasa tidak membutuhkan coding; helper Python bersifat opsional.

> Secara default, skill langsung mengerjakan permintaan. Saat diminta memperbaiki email, hasilnya seharusnya email yang sudah diperbaiki, bukan petunjuk cara memperbaikinya. Prompt baru dibuat ketika diminta. Menyiapkan konten tidak otomatis memberi izin untuk mengirim atau memublikasikannya.

## Tujuan dan manfaatnya

**Tujuannya adalah mengurangi usaha dari “saya butuh bantuan untuk ini” sampai mendapatkan hasil yang bisa digunakan.** Skill dirancang agar permintaanmu lebih mudah dikerjakan sambil menjaga fakta, maksud, dan batasan yang kamu berikan.

| Kendala sehari-hari | Bantuan dari skill |
| --- | --- |
| Tahu kebutuhanmu, tetapi bingung menyusun prompt yang detail. | Memulai dari permintaan dan konteks yang tersedia; bertanya secara terarah hanya ketika informasi penting belum ada. |
| Jawaban terlalu umum, terlalu panjang, atau formatnya tidak sesuai. | Menggunakan ketentuan audiens, gaya bahasa, panjang, bahasa, dan format untuk menyusun hasil. |
| Harus menjelaskan proyek atau brand yang sama berulang kali. | Kamu bisa memilih Project Profile lokal yang memuat preferensi dan fakta bersumber untuk dipakai ulang. |
| Membutuhkan beberapa hasil terkait, tetapi faktanya tidak konsisten. | Outcome Packs memakai fakta sumber yang sama untuk menyiapkan beberapa draf yang selaras. |
| Minta satu bagian diperbaiki, tetapi seluruh tulisan malah berubah. | Repair Mode menetapkan bagian yang boleh berubah dan yang harus tetap; helper teks opsional memeriksa batas revisi secara persis. |
| Informasi yang belum ada malah menjadi tanggal, harga, atau janji karangan. | Mengarahkan agent untuk membedakan fakta yang diberikan, asumsi, dan hal yang belum diketahui. |

Ini adalah cara kerja yang dirancang untuk membantu, bukan jaminan jawaban selalu benar atau klaim penghematan waktu yang sudah diukur. Tetap periksa fakta dan komitmen penting sebelum menggunakan hasilnya.

## Cocok untuk siapa?

Siapa pun yang memakai agent AI yang kompatibel untuk pekerjaan atau belajar sehari-hari: pekerja yang mengurus pesan dan rapat, pelajar yang belajar dari catatan, kreator yang menyiapkan konten, freelancer dan pemilik usaha yang berkomunikasi dengan pelanggan, serta tim produk atau developer yang merapikan ide menjadi tugas. Kamu tidak harus menjadi developer untuk memakai workflow menulis, belajar, atau menyusun rencana.

## Contoh penggunaan sehari-hari

Setelah terpasang, panggil **@btr**, lalu jelaskan tugas dan tempelkan atau lampirkan bahan yang relevan. Contoh berikut bisa kamu sesuaikan dengan kebutuhan; bentuk hasilnya merupakan tujuan penggunaan, bukan hasil benchmark.

| Situasi | Contoh permintaan | Hasil yang berguna |
| --- | --- | --- |
| Ingin menolak undangan dengan sopan. | “@btr bantu saya menolak undangan ini dengan ramah. Buat singkat dan jangan mengarang alasan.” | Balasan sopan tanpa alasan palsu atau komitmen baru. |
| Perlu menanyakan perkembangan pekerjaan. | “@btr buat pesan follow-up ini ramah tetapi jelas. Pertahankan tenggat yang sudah ada di draf saya.” | Pesan siap ditinjau dengan permintaan dan tenggat asli tetap utuh. |
| Catatan rapat masih berantakan. | “@btr jadikan catatan ini keputusan, tugas, penanggung jawab, dan tenggat. Tandai yang belum disepakati.” | Ringkasan tindakan yang membedakan penugasan pasti dan pertanyaan terbuka. |
| Ada materi belajar yang sulit dipahami. | “@btr jelaskan materi ini untuk pemula, beri satu contoh konkret, lalu buat tiga soal latihan.” | Penjelasan dan latihan singkat berdasarkan bahan yang diberikan. |
| Pekerjaan minggu ini terlalu banyak. | “@btr ini daftar tugas, tenggat, dan waktu luang saya yang hanya enam jam. Pilih tiga prioritas dan apa yang ditunda.” | Usulan rencana sesuai kapasitasmu, tanpa mengubah kalender. |
| Dokumen panjang sulit ditindaklanjuti. | “@btr rangkum dokumen ini: apa yang berubah, apa yang harus saya lakukan, dan apa yang belum jelas.” | Poin penting dan langkah berikutnya, dengan informasi yang belum tersedia ditandai. |
| Ada pelanggan yang menyampaikan keluhan. | “@btr buat balasan yang tenang berdasarkan keluhan dan kebijakan layanan ini. Jangan menjanjikan refund atau tanggal kirim yang belum pasti.” | Draf yang empatik dengan langkah berikutnya yang didukung informasi. |
| Satu update produk perlu diumumkan di beberapa tempat. | “@btr ubah catatan rilis ini menjadi satu email pelanggan dan dua postingan sosial. Gunakan fakta produk yang sama.” | Draf yang konsisten dan disesuaikan untuk tiap kanal. |
| Ide fitur belum cukup jelas untuk diteruskan ke tim. | “@btr jadikan ide ini brief, alur pengguna, kriteria penerimaan, dan tugas implementasi. Jangan coding dulu.” | Bahan kerja yang terstruktur, termasuk keputusan yang belum selesai. |
| Draf sudah bagus, tetapi pembukanya kurang pas. | “@btr ubah pembukanya saja. Pertahankan teks lainnya dan ajakan bertindak tanpa perubahan.” | Revisi terarah, bukan penulisan ulang seluruh draf yang tidak diperlukan. |

Tugas sederhana tidak membutuhkan Outcome Pack lengkap atau Project Profile. Mulai dari hasil terkecil yang menyelesaikan kebutuhanmu; gunakan struktur tambahan ketika memang diperlukan.

### Seperti apa contoh hasilnya?

Contoh di bawah bersifat fiktif untuk menunjukkan bentuk hasil yang dituju, bukan rekaman evaluasi model.

<details>
<summary><strong>Contoh 1: pesan mentah menjadi follow-up yang sopan</strong></summary>

**Draf kamu:**

> hai Sam gimana draf yang katanya mau dikirim kemarin? saya perlu hari ini

**Permintaan kamu:**

> @btr buat pesan ini ramah dan profesional. Tetap singkat dan pertahankan tenggat yang sudah ada.

**Ilustrasi hasil:**

> Hai Sam, saya ingin menanyakan draf yang rencananya dikirim kemarin. Saya membutuhkannya hari ini. Boleh dibantu kabar perkembangannya? Terima kasih!

Hasilnya mempertahankan permintaan dan waktu yang memang ada, tanpa menambahkan rapat, alasan, atau janji baru.

</details>

<details>
<summary><strong>Contoh 2: catatan rapat acak menjadi ringkasan tindakan</strong></summary>

**Catatan kamu:**

> Alex membuat draf proposal. Morgan memeriksa. Anggaran belum diputuskan. Belum ada tenggat yang disepakati.

**Permintaan kamu:**

> @btr ambil tugas, penanggung jawab, tenggat, dan keputusan terbuka. Jangan mengisi informasi yang belum ada.

**Ilustrasi hasil:**

| Tugas | Penanggung jawab | Tenggat |
| --- | --- | --- |
| Membuat draf proposal | Alex | Belum disepakati |
| Memeriksa proposal | Morgan | Belum disepakati |

**Keputusan terbuka:** anggaran belum diputuskan.

Catatan menjadi lebih mudah ditindaklanjuti tanpa mengarang anggaran atau tenggat.

</details>

## Mulai dari pekerjaan nyata

Setelah skill dipasang, minta kepada agent:

```text
@btr Launch Kit.
Ubah catatan rilis ini menjadi satu email pelanggan dan dua postingan sosial.
Gunakan hanya fakta yang tersedia. Tulis dalam bahasa Indonesia.
Siapkan draf saja, jangan publikasikan.
```

```text
@btr gunakan profil proyek .btr/profiles/northstar.json.
Jadikan ide fitur ini requirement, user flow, acceptance criteria,
dan tugas implementasi berurutan. Tandai keputusan yang belum selesai.
Jangan mulai coding.
```

```text
@btr Repair Mode.
Ubah paragraf pembuka saja. Pertahankan semua fakta produk, paragraf lainnya,
dan CTA tanpa perubahan. Berikan draf lengkap setelah revisi.
```

Contoh ini memakai paket nama pendek yang sudah dipasang. Gunakan `$btr` di Codex CLI/IDE; instalasi nama panjang tetap memakai `$brief-to-result`. Contoh dokumentasi bukan bukti kompatibilitas semua aplikasi.

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

### Nama pendek: btr (disarankan)

Sumber utama tetap di `brief-to-result/`. Builder menghasilkan **skill `btr` yang lengkap dan mandiri**, bukan pemanggil yang membutuhkan skill kedua. Nama skill dan prompt pemanggilan diubah, sementara seluruh panduan, helper, dan lisensi MIT tetap disertakan.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
python3 tools/build_btr.py --output dist/btr.zip
```

Untuk akun ChatGPT yang menyediakan unggah skill, impor `dist/btr.zip` melalui **Plugins → Skills → Create → Upload from your computer**, lalu tinjau dan pasang. Setelah aktif, ketik `@` dan pilih **BTR — Brief to Result**. Ketersediaan dan instalasi diatur aplikasi; publikasi GitHub tidak otomatis memasangnya ke akunmu.

Untuk pemasangan lokal pertama pada agent yang mendukung `~/.agents/skills/`, bangun langsung ke direktori baru:

```bash
python3 tools/build_btr.py --directory "$HOME/.agents/skills/btr"
```

Builder menolak lokasi yang sudah ada dan tidak menimpa instalasi lama. Periksa/cadangkan versi lama sebelum menggantinya. Gunakan lokasi sesuai dokumentasi client jika berbeda. Di Codex CLI/IDE, pilih `$btr` atau buka `/skills`. Sebaiknya aktifkan satu instalasi agar tidak muncul entri ganda.

### Instalasi nama panjang yang sudah ada

`brief-to-result/` dan `$brief-to-result` tetap didukung. Menyalin direktori asli memasang nama panjang, bukan skill native bernama `btr`. Jangan hanya mengganti nama folder: nama direktori dan metadata harus cocok. Gunakan builder untuk nama pendek. Pencocokan teks `@btr` pada instalasi nama panjang bergantung pada agent yang menemukan dan menerapkan deskripsi skill; ini bukan alias menu universal.

Simpan profil proyek di luar direktori instalasi skill. Instruksi Markdown bisa diikuti tanpa Python. Pembuatan paket nama pendek dan helper `btr.py` membutuhkan **Python 3.10+**, hanya memakai standard library, dan tidak memanggil jaringan/model. Kamu tetap membutuhkan agent yang kompatibel beserta akses modelnya; ini bukan chatbot mandiri atau layanan otomatisasi latar belakang.

Lihat [panduan pemanggilan](brief-to-result/references/invocation.md) untuk dokumentasi resmi aplikasi dan contoh pengujian manual.

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

Tes otomatis memeriksa paket nama pendek mandiri, helper lokal, penanganan error, kesegaran fakta, batas revisi teks, integritas katalog, dan tautan dokumentasi lokal. [Contoh pengujian manual](examples/README.md) mencakup tiga pack, prioritas bahasa, dan revisi terarah. Contoh itu bukan hasil benchmark model yang sudah diukur. Lulus tes lokal tidak membuktikan perilaku identik di semua agent, kebenaran fakta, atau peningkatan performa penjualan/konten.

Kode keluar helper: `0` berhasil, `1` ada fakta yang disisihkan saat pemeriksaan profil strict, `2` input tidak valid atau gagal menulis. Helper lama `text_metrics.py` memakai `1` ketika batas panjang gagal dipenuhi. Sumber yang berubah setelah rencana revisi dibuat membutuhkan rencana baru; file asli tidak pernah ditimpa.

## Lisensi dan perubahan

[MIT](LICENSE), copyright (c) 2026 makanSukros. [Salinan lisensi](brief-to-result/LICENSE) ikut dalam pemasangan skill mandiri. Lihat [CHANGELOG.md](CHANGELOG.md) untuk perubahan versi sumber.
