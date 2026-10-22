# Brief to Result

**Lebih sedikit menyusun prompt. Lebih banyak pekerjaan selesai.**

[English](README.md) | [Bahasa Indonesia](README.id.md) · [Lisensi MIT](LICENSE)

**Ubah permintaan sehari-hari menjadi hasil yang bisa dipakai:** hook affiliate untuk dikembangkan, balasan pelanggan yang siap diperiksa, draf konten, catatan rapat yang rapi, latihan belajar, atau brief fitur yang bisa diteruskan ke tim.

BTR adalah skill reusable untuk agent AI yang kompatibel, bukan chatbot terpisah atau model AI baru. Isinya **80 workflow, Hook Lab dengan 24 formula kreatif, tiga Outcome Packs, Project Profiles opsional, dan Repair Mode**. Kamu cukup menjelaskan hasil yang dibutuhkan, tanpa menghafal nama fitur atau nomor workflow.

[Cari contoh sesuai kebutuhanmu](#use-cases) · [Cara pakai](#quick-start) · [Fitur](#features) · [Instalasi](#instalasi) · [Alat bantu lokal](#local-tools)

## Tujuan dan manfaatnya

Tujuannya adalah mempersingkat proses dari **“tolong bantu saya”** menjadi hasil yang bisa digunakan. BTR dirancang untuk membantu agent memahami permintaan singkat, mengikuti bahasa dan formatmu, menjaga konsistensi beberapa draf, serta merevisi hanya bagian yang kamu minta.

BTR bekerja dari konteks dan bahan yang kamu berikan. Kalau informasi penting belum ada, agent diarahkan bertanya seperlunya, bukan mengarang harga, tenggat, fitur produk, atau pengalaman memakai barang. Ini adalah cara kerja untuk membantu, bukan jaminan jawaban sempurna, konten viral, penjualan naik, atau penghematan waktu yang sudah diukur.

> **Langsung ke hasil.** Minta perbaikan pesan, hasilnya pesan yang sudah diperbaiki—bukan prompt yang lebih panjang. Template prompt dibuat ketika diminta. Menyiapkan draf tidak otomatis berarti boleh mengirim atau memublikasikannya.

<a id="quick-start"></a>
## Cukup panggil @btr

Setelah skill dipasang dan dipilih pada aplikasi yang mendukungnya, ngobrol seperti biasa:

```text
@btr buatin 12 hook affiliate buat produk ini. Sudutnya harus beda-beda.
```

```text
tolong bantu balas pelanggan ini, tenang tapi jelas @btr
```

```text
@btr pembukanya aja yang diperbaiki. Bagian lain jangan diubah.
```

Tempelkan atau lampirkan detail produk, pesan, catatan, atau file yang relevan. BTR memakai konteks yang sudah tersedia; kamu tidak perlu mengulang brief di setiap revisi. Kalau belum ada tugas atau konteks, cukup satu pertanyaan singkat. Ketik `@btr menu` hanya saat ingin melihat pilihan.

**Mention bukan instalasi otomatis.** Pemilihan skill mengikuti aplikasi yang dipakai. Gunakan pemilih skill yang sudah terpasang jika diperlukan; client dengan pemanggilan berawalan dolar menggunakan `$btr`. Lihat [panduan pemanggilan](brief-to-result/references/invocation.md). Skill tidak menambahkan akses browsing, pembuatan gambar, file, atau izin publikasi jika agent memang tidak memilikinya.

<a id="use-cases"></a>
## Pilih contoh sesuai pekerjaanmu

Cari kategori yang paling dekat, salin contoh perintahnya, lalu sertakan bahan yang disebutkan. **Kategori ini bukan mode yang harus diatur terlebih dahulu.** Contoh lanjutan memakai bahan dari percakapan sebelumnya.

| Kamu sedang bekerja sebagai… | Langsung ke contoh | Hasil yang bisa diminta |
| --- | --- | --- |
| Affiliator | [Affiliator](#affiliates) | Hook berbeda angle, naskah demo, revisi pembuka |
| Seller atau pemilik UMKM | [Seller dan UMKM](#sellers) | Deskripsi produk, balasan keberatan, pengumuman peluncuran |
| Kreator atau pengelola media sosial | [Kreator dan Social Media](#creators) | Postingan, carousel, adaptasi konten |
| Marketer atau copywriter | [Marketing dan Copywriting](#marketing) | Angle iklan, headline landing page, rencana A/B test |
| Freelancer atau agency | [Freelancer dan Agency](#freelancers) | Proposal, komunikasi klien, batas revisi |
| Customer service atau admin | [Customer Service dan Admin](#support) | Balasan, FAQ, catatan eskalasi |
| Pekerja, manajer, atau pemimpin tim | [Pekerja dan Manajer Tim](#teams) | Ringkasan rapat, prioritas, SOP |
| Pelajar, mahasiswa, atau pengajar | [Belajar dan Mengajar](#learning) | Penjelasan, soal latihan, rencana pembelajaran |
| Founder, tim produk, atau developer | [Founder, Product, dan Developer](#product) | Validasi ide, spesifikasi fitur, diagnosis bug |
| Pengguna untuk kebutuhan pribadi | [Kebutuhan Sehari-hari](#everyday) | Pesan yang jelas, rencana praktis, perbandingan pilihan |

<a id="affiliates"></a>
### Contoh pemakaian untuk Affiliator

**Bisa membantu:** menemukan sudut jualan, membuka video produk, menyusun adegan demo, dan memperbaiki hook tanpa merombak seluruh naskah.

**Bahan yang berguna:** fungsi produk, siapa yang memakainya, spesifikasi yang diketahui, promo yang benar-benar berlaku, serta pengalamanmu sendiri jika ingin membuat review personal. Link atau foto produk membantu jika agent bisa membacanya. Tidak harus lengkap semua untuk mulai.

**1. Cari hook dengan angle yang berbeda**

```text
@btr buatin 12 hook affiliate buat penjepit kabel meja yang menahan ujung kabel
di tepi meja. Targetnya orang yang kerja di meja. Bahasa Indonesia,
natural, sedikit nyindir, dan pakai situasi sehari-hari yang beda-beda.
Jangan ngarang harga, popularitas, atau pengalaman pakai. Hooknya aja.
```

**2. Lanjutkan jadi konsep video yang bisa direkam**

```text
@btr pilih tiga hook paling menarik dari tadi.
Masing-masing jadiin naskah video singkat: pembuka, adegan pertama,
demo produk, dan satu CTA. Target sekitar 20 detik;
durasinya perkiraan dulu sampai dibaca. Saya bisa dapat komisi affiliate,
jadi sertakan keterangan yang jelas di naskahnya.
```

**3. Perbaiki pembuka yang masih terasa generik**

```text
@btr hook ini masih berasa iklan template. Ubah hooknya aja
pakai kejadian sehari-hari yang lebih spesifik dan ngena.
Fakta produk, isi naskah, dan CTA tetap. Jangan bikin testimoni palsu.
```

**Hasil yang didapat:** alasan memperhatikan produk yang berbeda-beda, hubungan yang jelas antara hook dan demo, serta revisi sesuai bagian yang diminta.

**Ilustrasi, bukan hasil benchmark:** untuk contoh fiktif penjepit kabel di atas, kalimat umum “Alat kecil ini bikin hidup lebih mudah” bisa dikembangkan menjadi **“Mejanya udah estetik. Nyari kabelnya masih harus merangkak.”** Adegan berikutnya perlu memperlihatkan masalah kabel dan fungsi penjepit yang sebenarnya, bukan kejutan yang tidak berhubungan.

[Hook Lab](brief-to-result/references/hook-lab.md) membangun hook dari situasi dan fungsi produk, bukan mengganti nama barang dalam daftar kalimat populer. Ada [24 formula](brief-to-result/references/hook-formulas.md) untuk masalah sehari-hari, kontras, demonstrasi, pertimbangan membeli, pengalaman nyata, dan interaksi. Kalau klaim urgensi atau performa belum didukung fakta, pendekatannya diganti—bukan buktinya dikarang. Lihat [contoh tambahan](brief-to-result/references/hook-examples.md).

<a id="sellers"></a>
### Contoh pemakaian untuk Seller dan UMKM

**Bisa membantu:** menjelaskan manfaat produk, menjawab keraguan pembeli, dan menyiapkan pengumuman yang konsisten.

**Bahan yang berguna:** deskripsi produk, target pembeli, harga dan syarat yang berlaku, atau pesan pelanggan.

**1. Ubah spesifikasi menjadi deskripsi yang mudah dipahami**

```text
@btr tulis ulang deskripsi produk ini untuk pembeli pertama kali.
Jelaskan setiap fitur penting membantu masalah sehari-hari yang mana.
Spesifikasi, harga, dan keterbatasannya jangan diubah.
Berikan satu deskripsi siap pakai, bukan tips menulis.
```

**2. Balas pelanggan yang bilang “mahal”**

```text
@btr bantu balas pelanggan yang bilang produk ini mahal.
Buat singkat dan ramah, pakai manfaat serta ketentuan produk yang saya berikan.
Jangan mengarang diskon atau memaksa orang membeli.
```

**3. Siapkan pengumuman peluncuran**

```text
@btr dari catatan rilis dan ketentuan penawaran yang sudah pasti ini,
buat satu email pelanggan, dua postingan sosial, dan lima jawaban FAQ.
Fakta produknya harus sama di semua draf. Jangan dipublikasikan dulu.
```

**Hasil yang didapat:** copy yang menjawab kebutuhan pembeli dan beberapa draf dengan informasi produk yang konsisten.

<a id="creators"></a>
### Contoh pemakaian untuk Kreator dan Social Media

**Bisa membantu:** mencari angle, mengubah bahan menjadi draf sesuai kanal, dan mempertahankan gaya penulisanmu.

**Bahan yang berguna:** topik, artikel, transkrip, postingan lama, atau contoh tulisanmu.

**1. Ubah artikel menjadi postingan singkat**

```text
@btr dari artikel ini, buat dua postingan X dalam bahasa Inggris.
Buka dengan poin paling menarik yang memang didukung artikel.
Pertahankan gaya ngobrol saya dan catatan penting dari sumbernya.
Jangan bikin hook yang janjinya tidak dijawab isi postingan.
```

**2. Susun carousel yang alurnya enak diikuti**

```text
@btr jadikan catatan ini carousel enam slide untuk pemula.
Setiap slide cukup satu ide utama, teks layar singkat, dan arahan visual.
Slide pertama harus spesifik, jangan cuma “Semua yang perlu kamu tahu”.
```

**3. Adaptasi satu video menjadi beberapa konten**

```text
@btr dari transkrip ini, buat satu postingan LinkedIn, satu caption Instagram,
dan satu outline video pendek. Faktanya sama, tapi angle dan susunannya
sesuaikan masing-masing kanal. Berikan draf, bukan jadwal posting.
```

**Hasil yang didapat:** draf berbeda yang sesuai kanal. Arahan visual atau outline bukan gambar maupun video jadi; produksi membutuhkan alat yang tersedia dan permintaan untuk membuatnya.

<a id="marketing"></a>
### Contoh pemakaian untuk Marketing dan Copywriting

**Bisa membantu:** mencari alasan membeli yang berbeda, memperjelas pesan produk, dan merancang perbandingan materi iklan.

**Bahan yang berguna:** audiens, penawaran, bukti produk, landing page, dan batasan kampanye.

**1. Cari beberapa sudut iklan untuk satu penawaran**

```text
@btr buat lima angle iklan untuk penawaran dan audiens ini.
Masing-masing harus menjawab masalah, keraguan, atau motivasi membeli yang berbeda.
Beri satu headline dan satu kalimat pembuka per angle.
Jangan tambahkan klaim paling bagus tanpa bukti.
```

**2. Perjelas bagian pertama landing page**

```text
@btr perbaiki hero section landing page ini saja.
Harus langsung jelas produknya untuk siapa, membantu apa, dan langkah berikutnya.
Pertahankan penawaran serta klaim yang sebenarnya. Pilih satu versi rekomendasi.
```

**3. Rancang pengujian dua hook**

```text
@btr susun A/B test untuk dua kalimat pembuka ini.
Jaga audiens, penawaran, isi, dan CTA tetap sebanding.
Jelaskan dugaan yang diuji, metrik yang diamati, dan batas kesimpulannya.
Jangan meramal CTR pemenangnya.
```

**Hasil yang didapat:** konsep yang benar-benar berbeda dan alasan pengujian yang jelas, bukan skor performa karangan.

<a id="freelancers"></a>
### Contoh pemakaian untuk Freelancer dan Agency

**Bisa membantu:** merapikan permintaan klien menjadi lingkup kerja dan menyampaikan batas pekerjaan tanpa terkesan menyerang.

**Bahan yang berguna:** brief klien, hasil yang disepakati, tenggat, biaya, serta ketentuan revisi yang memang ada.

**1. Susun draf proposal dari brief**

```text
@btr jadikan brief klien ini proposal singkat berisi tujuan,
hasil yang diserahkan, hal di luar lingkup, kebutuhan dari klien, dan pertanyaan terbuka.
Biaya serta timeline pakai yang memang sudah disepakati. Tandai yang belum pasti.
```

**2. Balas permintaan tambahan di luar lingkup**

```text
@btr bantu balas permintaan tambahan ini dengan ramah tapi tegas.
Jelaskan bagian yang di luar scope terlampir dan apa yang perlu disepakati
sebelum dikerjakan. Jangan menjanjikan gratis atau mengarang biaya baru.
```

**3. Terapkan revisi tanpa mengubah bagian yang sudah disetujui**

```text
@btr terapkan feedback klien ini pada headline dan paragraf penutup saja.
Isi utama yang sudah disetujui, fakta produk, dan hasil kerja tetap.
Berikan draf revisi dan ringkasan singkat bagian yang berubah.
```

**Hasil yang didapat:** bahan kerja yang lebih jelas, balasan klien siap ditinjau, atau revisi terarah. Menulis proposal tidak otomatis mengirim atau menyetujui perjanjian.

<a id="support"></a>
### Contoh pemakaian untuk Customer Service dan Admin

**Bisa membantu:** membalas dengan empati, menjelaskan langkah berikutnya, dan merapikan pertanyaan berulang menjadi panduan.

**Bahan yang berguna:** pesan pelanggan yang sudah disamarkan, kebijakan layanan, fakta masalah yang diketahui, atau catatan support yang disetujui.

**1. Balas keluhan tanpa menjanjikan yang belum pasti**

```text
@btr buat balasan yang tenang untuk keluhan ini berdasarkan kebijakan layanan terlampir.
Akui masalahnya, jelaskan langkah berikutnya yang memang tersedia,
dan tanyakan hanya informasi yang diperlukan.
Jangan mengarang refund atau waktu penyelesaian.
```

**2. Jadikan pertanyaan berulang sebagai FAQ**

```text
@btr kelompokkan pertanyaan pelanggan yang sudah disamarkan ini menjadi FAQ.
Jawab berdasarkan dokumentasi yang saya berikan.
Tandai pertanyaan yang belum terjawab di dokumentasi, jangan bikin kebijakan baru.
```

**3. Buat catatan eskalasi internal**

```text
@btr rangkum percakapan support ini untuk diteruskan ke tim internal:
masalah yang dilaporkan, bukti yang terlihat, langkah yang sudah dicoba,
dampak ke pelanggan, dan informasi yang masih dibutuhkan.
Pisahkan fakta pasti dan dugaan penyebab.
```

**Hasil yang didapat:** draf balasan dan catatan internal yang mudah ditindaklanjuti. Hapus data pribadi yang tidak diperlukan sebelum membagikan bahan; tidak ada pesan yang otomatis dikirim.

<a id="teams"></a>
### Contoh pemakaian untuk Pekerja dan Manajer Tim

**Bisa membantu:** mengubah rapat menjadi tindakan, menentukan prioritas yang realistis, dan membuat proses kerja yang bisa diulang.

**Bahan yang berguna:** catatan rapat, daftar tugas beserta tenggat dan kapasitas, atau penjelasan proses yang sedang berjalan.

**1. Rapikan catatan rapat menjadi tindakan**

```text
@btr jadikan catatan rapat ini keputusan, tugas, penanggung jawab, dan tenggat.
Kalau penanggung jawab atau tanggalnya belum ada, tulis belum disepakati.
Pisahkan pertanyaan terbuka. Jangan menambahkan komitmen yang tidak ada di catatan.
```

**2. Pilih pekerjaan yang muat minggu ini**

```text
@btr ini daftar tugas dan tenggat saya. Minggu ini waktu tersedia cuma enam jam.
Pilih tiga prioritas, apa yang ditunda, dan konsekuensi pilihannya.
Jelaskan mana estimasi waktu yang masih perkiraan. Jangan ubah kalender saya.
```

**3. Buat SOP yang bisa diikuti anggota baru**

```text
@btr ubah penjelasan proses ini menjadi SOP untuk anggota tim baru.
Cantumkan kapan dimulai, bahan yang dibutuhkan, langkah kerja, pengecualian,
alur eskalasi, dan tanda pekerjaan selesai. Tandai keputusan kebijakan yang belum ada.
```

**Hasil yang didapat:** rencana atau prosedur dengan langkah berikutnya yang jelas, tanpa mengarang keputusan untuk tim.

<a id="learning"></a>
### Contoh pemakaian untuk Pelajar, Mahasiswa, dan Pengajar

**Bisa membantu:** memahami materi sulit, berlatih menjawab, dan menyiapkan pembelajaran dengan tujuan yang jelas.

**Bahan yang berguna:** catatan, cuplikan bab, tujuan belajar, tingkat pemahaman peserta, atau jawaban yang sudah kamu coba.

**1. Pahami bagian materi yang membingungkan**

```text
@btr jelaskan bagian catatan ini untuk pemula.
Mulai dari ide utamanya, kasih satu contoh konkret, lalu jelaskan
kesalahpahaman yang paling mungkin terjadi. Detail teknisnya harus tetap benar.
```

**2. Latihan dulu sebelum melihat jawaban**

```text
@btr buat lima soal latihan dari catatan ini, dari mudah ke lebih sulit.
Berikan soalnya dulu dan tunggu jawaban saya sebelum menunjukkan pembahasan.
Jangan memasukkan materi di luar catatan tanpa menandainya sebagai tambahan.
```

**3. Siapkan pembelajaran yang terarah**

```text
@btr gunakan bahan ini untuk membuat rencana pembelajaran 30 menit
sesuai tingkat peserta yang saya sebutkan. Sertakan satu tujuan belajar,
penjelasan, aktivitas, dan pemeriksaan pemahaman.
Durasi itu rencana, bukan waktu yang sudah diuji.
```

**Hasil yang didapat:** penjelasan, latihan, atau rencana mengajar berdasarkan bahan yang tersedia, bukan kutipan atau referensi karangan.

<a id="product"></a>
### Contoh pemakaian untuk Founder, Product, dan Developer

**Bisa membantu:** menguji ide, memperjelas perilaku fitur sebelum dibangun, dan mencari penyebab bug berdasarkan bukti.

**Bahan yang berguna:** masalah dan target pengguna, catatan fitur, alur saat ini, kode, log, atau langkah reproduksi error.

**1. Uji ide sebelum terlalu banyak membangun**

```text
@btr bedah ide produk ini. Cari tiga asumsi paling berisiko,
bukti yang bisa mendukung atau menggugurkan masing-masing,
dan eksperimen kecil yang sebaiknya dilakukan lebih dulu.
Jangan menganggap kebutuhan pasarnya sudah terbukti.
```

**2. Jadikan ide fitur bahan implementasi**

```text
@btr ubah ide fitur ini menjadi brief, alur pengguna, acceptance criteria,
edge cases, dan tugas implementasi berurutan sesuai dependensinya.
Tandai keputusan yang masih perlu dibuat. Jangan coding dulu.
```

**3. Diagnosis bug sebelum memberi patch**

```text
@btr periksa error, kode terkait, dan langkah reproduksi ini.
Pisahkan fakta yang terlihat dari dugaan. Pilih pemeriksaan pertama yang paling berguna,
lalu jika buktinya cukup, sarankan perbaikan terarah dan cara mengujinya.
```

**Hasil yang didapat:** rencana eksperimen, spesifikasi implementasi, atau diagnosis berbasis bukti. Saran perbaikan belum berarti perbaikan sudah diuji; BTR harus membedakannya.

<a id="everyday"></a>
### Contoh pemakaian untuk Kebutuhan Sehari-hari

**Bisa membantu:** menyampaikan maksud dengan jelas, mempertimbangkan pilihan, dan merapikan kebutuhan menjadi rencana yang masuk akal.

**Bahan yang berguna:** pesan yang perlu dijawab, batasanmu, atau pilihan yang sedang dipertimbangkan.

**1. Tolak undangan dengan sopan**

```text
@btr bantu saya menolak undangan ini dengan ramah dalam dua kalimat.
Jangan mengarang alasan atau menawarkan tanggal pengganti yang belum saya setujui.
```

**2. Atur pekerjaan rumah untuk akhir pekan**

```text
@btr susun pekerjaan rumah ini sesuai waktu empat jam yang saya punya hari Sabtu.
Kelompokkan tugas yang berkaitan, sisakan sedikit jeda,
dan jelaskan apa yang ditunda kalau tidak semuanya muat.
Jangan menjadwalkan apa pun di aplikasi.
```

**3. Bandingkan pilihan berdasarkan kebutuhanmu**

```text
@btr bandingkan tiga pilihan ini dengan budget dan prioritas saya.
Rekomendasikan satu, jelaskan konsekuensinya, dan informasi apa yang belum ada
sehingga bisa mengubah pilihan. Pakai fakta yang saya berikan, bukan spesifikasi karangan.
```

**Hasil yang didapat:** draf siap ditinjau, usulan rencana yang realistis, atau perbandingan yang menjelaskan ketidakpastiannya.

<a id="features"></a>
## Fitur di balik contoh-contoh tadi

Tidak perlu memilih fitur secara manual. BTR mengarahkan cara kerja berdasarkan hasil yang kamu minta.

| Fitur | Manfaat | Panduan |
| --- | --- | --- |
| **Hook Lab** | 24 formula kreatif untuk hook jualan dan affiliate, pemeriksaan variasi, serta hubungan hook dengan demo | [Hook Lab](brief-to-result/references/hook-lab.md) |
| **Outcome Packs** | Beberapa hasil yang saling terkait memakai satu kumpulan fakta | [Protokol pack](brief-to-result/references/outcome-packs.md) |
| **Project Profiles** | Preferensi dan fakta proyek bersumber yang dipilih secara eksplisit | [Panduan profil](brief-to-result/references/project-profiles.md) |
| **Repair Mode** | Revisi terarah sambil menjaga teks dan bagian di luar lingkup | [Panduan revisi](brief-to-result/references/repair-mode.md) |
| **80 workflow** | Penulisan, pemahaman, ide, penjualan, konten, produk, teknis, dan operasional | [Instruksi utama](brief-to-result/SKILL.md) |

24 formula hook melengkapi 80 workflow, bukan tambahan 24 workflow umum. Kegunaan kreatifnya tetap perlu dinilai dalam penggunaan nyata.

### Tiga Outcome Packs

| Pack | Hasil bawaan |
| --- | --- |
| [Launch Kit](brief-to-result/packs/launch-kit.md) | Pesan utama, email, draf sosial, FAQ, checklist peluncuran, sumber dan informasi terbuka |
| [Idea to Build](brief-to-result/packs/idea-to-build.md) | Brief, alur pengguna, acceptance criteria, tugas implementasi, keputusan terbuka |
| [Research to Content](brief-to-result/packs/research-to-content.md) | Peta sumber, rangkuman, angle, draf konten, catatan verifikasi |

Lingkup permintaanmu mengalahkan hasil bawaan. Satu email tidak otomatis menjadi kampanye lengkap. Pack dijalankan oleh agent; helper Python tidak menghasilkan konten atau memanggil model.

### Pakai ulang konteks proyek dan revisi dengan tepat

```text
@btr gunakan profil proyek .btr/profiles/northstar.json untuk pengumuman ini.
```

Profil bersifat opsional dan harus dipilih, bukan memori tersembunyi atau penyimpanan otomatis lintas chat. Instruksi tugas terbaru mengalahkan preferensi. Fakta produk memiliki sumber dan tanggal tinjauan; fakta yang disisihkan atau kedaluwarsa tidak boleh diam-diam mengisi kekosongan. Label `confirmed` dikelola pengguna, bukan verifikasi independen. File lokal tidak dienkripsi dan isinya dapat dilihat model saat kamu meminta agent membacanya. Jangan simpan kredensial atau data pribadi pelanggan.

```text
@btr ringkas paragraf kedua saja. Harga, syarat, dan CTA jangan berubah.
```

Repair Mode memandu revisi agent. Helper teks UTF-8 opsional bisa memeriksa hash sumber, teks terkunci, dan batas perubahan, menampilkan diff, lalu menulis ke file baru saja. Makna dan gaya tetap perlu ditinjau; instruksi prompt saja bukan perlindungan deterministik.

## Instalasi

### Buat paket dengan nama pendek btr

Sumber utama berada di `brief-to-result/`. Builder membuat skill mandiri bernama `btr`, lengkap dengan panduan, helper, dan lisensi MIT.

```bash
git clone https://github.com/makanSukros/brief-to-result.git
cd brief-to-result
python3 tools/build_btr.py --output dist/btr.zip
```

Impor `dist/btr.zip` melalui proses pemasangan skill yang didukung aplikasimu, lalu aktifkan/pilih BTR. Lihat [panduan pemanggilan](brief-to-result/references/invocation.md) untuk langkah khusus aplikasi. Publikasi ke GitHub atau mengetik `@btr` tidak otomatis memasangnya ke akun.

Untuk pemasangan lokal pertama pada agent yang mendukung `~/.agents/skills/`:

```bash
python3 tools/build_btr.py --directory "$HOME/.agents/skills/btr"
```

Builder menolak lokasi yang sudah ada. Periksa/cadangkan instalasi lama sebelum menggantinya; gunakan lokasi sesuai dokumentasi client jika berbeda. Sebaiknya aktifkan satu instalasi agar tidak muncul entri ganda. Simpan profil proyek di luar direktori instalasi skill.

Instalasi `brief-to-result/` tetap didukung. Menyalin direktori utama memasang nama panjang, bukan `btr`; jangan sekadar mengganti nama folder karena nama direktori dan metadata harus sesuai. Gunakan builder untuk nama pendek. Lihat [detail pemanggilan](brief-to-result/references/invocation.md) untuk pemilihan nama panjang dan batas alias.

Instruksi Markdown bisa diikuti tanpa Python. Builder dan `btr.py` membutuhkan **Python 3.10+**, memakai standard library, dan tidak memanggil jaringan/model. Kamu tetap membutuhkan agent yang kompatibel beserta akses modelnya.

<a id="local-tools"></a>
## Alat bantu lokal opsional

Permintaan menulis, membuat hook, dan menyusun rencana biasa tidak mengharuskanmu menjalankan perintah ini. Contoh berikut dijalankan dari root repository hasil clone; untuk versi terpasang, ganti awalan `brief-to-result/` dengan lokasi sebenarnya.

<details>
<summary><strong>Cari pack dan workflow</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py packs list
python3 brief-to-result/scripts/btr.py packs show launch-kit
python3 brief-to-result/scripts/lookup.py --list
python3 brief-to-result/scripts/lookup.py --id W03
python3 brief-to-result/scripts/lookup.py --query "caption"
python3 brief-to-result/scripts/text_metrics.py --help
```

Perintah pack menampilkan instruksi, bukan menghasilkan konten. `--json` memberikan metadata pack yang bisa dibaca program.

| Bidang | ID |
| --- | --- |
| Penulisan dan penyuntingan | W01–W10 |
| Pemahaman dan pembelajaran | U01–U10 |
| Ide dan strategi | I01–I10 |
| Penjualan dan persuasi | M01–M10 |
| Konten dan storytelling | C01–C10 |
| Produk dan UX | P01–P10 |
| Pekerjaan teknis | T01–T10 |
| Operasional dan keputusan | O01–O10 |

Setiap workflow berisi pemicu, input, metode, bentuk hasil, pemeriksaan, dan contoh.

</details>

<details>
<summary><strong>Buat dan periksa profil proyek</strong></summary>

```bash
python3 brief-to-result/scripts/btr.py profiles init northstar
# Edit .btr/profiles/northstar.json dengan preferensi dan fakta proyek yang sebenarnya.
python3 brief-to-result/scripts/btr.py profiles check .btr/profiles/northstar.json
python3 brief-to-result/scripts/btr.py profiles context .btr/profiles/northstar.json
```

Inisialisasi menolak menimpa profil dan membuat file ignore lokal jika belum ada. Aturan ignore tidak melindungi file yang sudah dilacak Git; periksa `git status` sebelum commit. Tambahkan `--as-of YYYY-MM-DD` untuk pemeriksaan tanggal yang dapat diulang atau `--strict` pada `profiles check` agar pemeriksaan gagal jika ada fakta yang disisihkan. Lihat [template](brief-to-result/assets/profile.template.json) dan [aturan skema](brief-to-result/references/project-profiles.md).

</details>

<details>
<summary><strong>Preview dan terapkan revisi teks terarah</strong></summary>

Contoh Northstar yang disertakan bersifat fiktif. Buat rencana untuk baris pertamanya:

```bash
mkdir -p .btr
python3 brief-to-result/scripts/btr.py repair plan examples/repair-before.txt \
  --allow 1:1 --keep "Try the demo." --output .btr/repair.json
```

Edit hanya nilai `replacement` di `.btr/repair.json` dengan mempertahankan `\n` di ujungnya. Contoh: `Export your report without retyping it.\n`. Lalu:

```bash
python3 brief-to-result/scripts/btr.py repair preview examples/repair-before.txt --plan .btr/repair.json
python3 brief-to-result/scripts/btr.py repair apply examples/repair-before.txt \
  --plan .btr/repair.json --output .btr/revised.txt
```

Ulangi `--allow START:END` untuk beberapa rentang baris sumber yang terpisah dan `--keep` untuk teks tambahan yang harus tetap persis. Preview tidak menulis file; apply menolak tujuan yang sudah ada. Helper menolak rencana kedaluwarsa serta rentang tidak valid atau bertumpuk. Hanya teks UTF-8, bukan dokumen biner. Rencana berisi cuplikan sumber; perlakukan sesuai kerahasiaan sumbernya. Batas lingkup adalah kontrak yang dapat ditinjau, bukan sandbox keamanan.

</details>

## Bahasa, bukti, dan batasan

Bahasa dasar skill dan [README utama](README.md) tetap Inggris; README Indonesia ini menyediakan jalur penggunaan yang sama. Hasil kerja mengikuti bahasa yang diminta dan konteks audiens yang sudah jelas. Teks yang disunting mempertahankan bahasa aslinya kecuali diminta diterjemahkan. Bahasa Inggris tidak berarti otomatis pasar AS, harga dolar, atau zona waktu tertentu.

Contoh adalah permintaan dan ilustrasi yang bisa disesuaikan, bukan testimoni atau hasil benchmark model. Periksa klaim penting sebelum publikasi. Pengalaman affiliate, promo, harga, kelangkaan stok, dan perbandingan harus punya dasar nyata. BTR diarahkan mengganti angle yang tidak didukung, bukan mengarang bukti. Keterangan hubungan komersial harus sesuai kenyataannya; skill bukan sertifikasi kepatuhan hukum semua negara.

Browsing, pembuatan media, integrasi, dan operasi file bergantung pada alat serta izin agent. Draf tidak otomatis dikirim, uang iklan tidak dibelanjakan, dan pekerjaan latar belakang tidak dibuat hanya karena disebut dalam workflow.

## Pengujian

```bash
python3 -m unittest discover -s tests -v
```

Tes mencakup helper lokal, paket instalasi, penanganan error, kesegaran profil, batas revisi, struktur katalog, dan sumber dokumentasi. Lihat [contoh pengujian manual](examples/README.md) serta [kasus Hook Lab](brief-to-result/references/hook-examples.md). Lulus tes lokal tidak membuktikan kreativitas, kebenaran fakta, perilaku identik di semua agent, atau peningkatan conversion.

Kode keluar helper: `0` berhasil, `1` ada fakta yang disisihkan saat pemeriksaan profil strict, `2` input tidak valid atau gagal menulis. `text_metrics.py` memakai `1` ketika pemeriksaan panjang gagal. Kalau sumber revisi berubah, buat rencana baru; file asli tidak pernah ditimpa helper revisi.

## Lisensi dan perubahan

[MIT](LICENSE), copyright (c) 2026 makanSukros. [Salinan lisensi](brief-to-result/LICENSE) ikut dalam pemasangan skill mandiri. Lihat [CHANGELOG.md](CHANGELOG.md) untuk perubahan versi sumber.
