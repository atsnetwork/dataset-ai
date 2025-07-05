import json
import random

def generate_chatbot_data(num_entries, start_id=1):
    data = []

    tipe_interaksi_options = ["pertanyaan", "kritik", "saran", "review"]

    departments_list = [ # Ubah nama variabel agar tidak ambigu dengan placeholder {departemen}
        "HRD", "Keuangan", "IT", "Pemasaran", "Operasional", "Produksi", "Legal",
        "Umum", "Penjualan", "R&D", "Desain", "Logistik", "Manajemen Proyek"
    ]

    # Kumpulan template teks interaksi dan jawaban ideal yang lebih luas dan bervariasi
    # Placeholder harus berupa string literal seperti "{topik}", bukan f-string
    interaction_templates = {
        "pertanyaan": [
            ("Bagaimana cara mengajukan {topik}?", "Untuk mengajukan {topik}, Anda dapat mengakses portal HRIS atau menghubungi tim HRD."),
            ("Kapan {topik} akan dibagikan/diumumkan?", "Informasi tentang {topik} biasanya akan diumumkan pada awal bulan atau melalui email resmi."),
            ("Apa kebijakan perusahaan tentang {topik}?", "Kebijakan {topik} dapat ditemukan di buku panduan karyawan, intranet, atau tanyakan ke departemen {departemen}."),
            ("Siapa yang bisa membantu saya dengan masalah {topik}?", "Anda bisa menghubungi {departemen} atau spesialis {topik} kami untuk bantuan lebih lanjut."),
            ("Bagaimana cara update data {topik} saya?", "Perubahan data {topik} dapat dilakukan melalui sistem HRIS, atau lapor ke HRD dengan menyertakan bukti pendukung."),
            ("Apakah {topik} termasuk dalam benefit kami?", "Ya, {topik} adalah salah satu benefit yang ditawarkan perusahaan. Detailnya ada di panduan benefit."),
            ("Dimana saya bisa menemukan informasi lebih lanjut tentang {topik}?", "Anda bisa menemukan informasi lebih lanjut di website internal atau bertanya langsung ke {departemen}."),
            ("Apa syarat untuk mengajukan {topik}?", "Syarat untuk {topik} meliputi {syarat_1} dan {syarat_2}. Detail lengkapnya di portal HR."),
            ("Apakah ada pelatihan tentang {topik} yang tersedia?", "Ya, kami sering mengadakan pelatihan {topik}. Informasi jadwal akan diumumkan oleh {departemen}."),
            ("Bagaimana prosedur kenaikan {topik}?", "Prosedur kenaikan {topik} melibatkan evaluasi kinerja dan persetujuan dari manajer serta HRD."),
            ("Apakah karyawan masih bekerja di {departemen}?", "Berdasarkan data kami, karyawan masih aktif di departemen {departemen}."),
            ("Berapa lama waktu yang dibutuhkan untuk proses {topik}?", "Estimasi waktu untuk proses {topik} adalah sekitar {waktu_proses} hari kerja."),
            ("Apakah ada formulir khusus untuk {topik}?", "Ya, formulir khusus untuk {topik} dapat diunduh dari intranet perusahaan.")
        ],
        "kritik": [
            ("Saya merasa {topik} di kantor kurang memadai/optimal.", "Terima kasih atas masukannya. Kami akan menindaklanjuti terkait kualitas {topik}."),
            ("Ada masalah berulang dengan {topik} yang sering terjadi.", "Kami akan investigasi secara menyeluruh dan mencari solusi untuk masalah {topik} ini."),
            ("Kualitas {topik} perlu ditingkatkan secara signifikan.", "Kritik Anda tentang {topik} akan menjadi perhatian utama kami dan akan dievaluasi."),
            ("Saya tidak puas dengan layanan {topik} yang diberikan.", "Mohon maaf atas ketidaknyamanan yang Anda alami. Kami akan segera memeriksa masalah {topik} ini."),
            ("Waktu respons untuk {topik} terlalu lama/lambat.", "Kami akan berusaha mempercepat proses {topik} ke depannya dan meningkatkan efisiensi."),
            ("Lingkungan kerja terasa tidak nyaman karena {topik}.", "Kami prihatin mendengar hal ini. Tim fasilitas akan segera memeriksa kondisi {topik} di area Anda."),
            ("Ada ketidakadilan dalam penerapan {topik} di perusahaan.", "Kami akan melakukan peninjauan terhadap penerapan {topik} untuk memastikan keadilan bagi semua karyawan."),
            ("Komunikasi dari manajemen terkait {topik} kurang jelas.", "Kami akan meneruskan masukan ini agar komunikasi terkait {topik} bisa lebih transparan di masa mendatang."),
            ("Program {topik} tidak efektif atau tidak relevan.", "Umpan balik Anda tentang efektivitas program {topik} akan menjadi bahan evaluasi kami."),
            ("Kinerja karyawan kurang memuaskan di area {topik}.", "Kami akan meneruskan umpan balik ini kepada manajer karyawan untuk ditindaklanjuti.")
        ],
        "saran": [
            ("Bagaimana jika kita menerapkan {topik} baru untuk meningkatkan produktivitas?", "Saran Anda mengenai penerapan {topik} sangat inovatif dan akan kami pertimbangkan."),
            ("Saya punya ide untuk meningkatkan {topik} agar lebih efisien.", "Terima kasih atas idenya, kami akan mengevaluasi bagaimana peningkatan {topik} ini dapat diimplementasikan."),
            ("Bisa dipertimbangkan untuk menambahkan fasilitas {topik} di kantor?", "Kami akan membahas usulan penambahan fasilitas {topik} dalam rapat tim fasilitas berikutnya."),
            ("Saran saya agar prosedur {topik} bisa lebih sederhana.", "Kami akan mencari cara agar prosedur {topik} bisa lebih efisien dan sederhana sesuai saran Anda."),
            ("Bagaimana jika ada program {topik} untuk pengembangan karyawan?", "Program {topik} adalah ide yang bagus untuk pengembangan. Kami akan diskusikan lebih lanjut dengan HRD."),
            ("Saya menyarankan agar {topik} dapat diakses secara online.", "Saran Anda untuk akses {topik} secara online akan kami pertimbangkan untuk kemudahan karyawan."),
            ("Perlu ada sosialisasi lebih lanjut tentang {topik}.", "Setuju, sosialisasi {topik} yang lebih intensif akan membantu. Kami akan rencanakan."),
            ("Bisakah kita mengadakan acara {topik} secara rutin?", "Ide acara {topik} rutin sangat menarik. Kami akan melihat kemungkinan pelaksanaannya."),
            ("Saran untuk karyawan agar lebih proaktif di {topik}.", "Terima kasih atas sarannya, akan kami sampaikan kepada karyawan."),
            ("Pertimbangkan untuk memperluas cakupan {topik} benefit kami.", "Kami akan mengevaluasi opsi untuk memperluas cakupan {topik} dalam paket benefit."),
            ("Bagaimana jika ada sesi feedback rutin terkait {topik}?", "Ide sesi feedback rutin untuk {topik} sangat konstruktif. Kami akan mengaturnya.")
        ],
        "review": [
            ("Kinerja karyawan di bidang {topik} sangat baik dan melebihi ekspektasi.", "Apresiasi Anda untuk karyawan akan kami sampaikan ke yang bersangkutan dan dicatat dalam rekam jejaknya."),
            ("Saya puas dengan kontribusi karyawan dalam {topik} proyek ini.", "Terima kasih atas ulasan positifnya, kami akan mencatat pencapaian karyawan yang luar biasa."),
            ("Tim karyawan sangat kooperatif dan responsif di {topik}.", "Kami senang mendengar tim karyawan bisa bekerja sama dengan baik dalam {topik}."),
            ("Performa karyawan perlu ditingkatkan di area {topik}.", "Kami akan meneruskan umpan balik ini kepada manajer karyawan untuk ditindaklanjuti dan rencana pengembangan."),
            ("Saya punya masukan konstruktif untuk karyawan terkait {topik}.", "Terima kasih atas masukannya, akan kami sampaikan kepada karyawan untuk perbaikan."),
            ("Dedikasi karyawan dalam menyelesaikan {topik} patut diacungi jempol.", "Kami sangat mengapresiasi dedikasi karyawan dalam menyelesaikan {topik}."),
            ("Perlu diperhatikan {topik} dari karyawan.", "Umpan balik terkait {topik} dari karyawan akan kami catat untuk evaluasi lebih lanjut.")
        ]
    }

    def get_random_placeholder(placeholder_type):
        if placeholder_type == "departemen":
            return random.choice(departments_list)
        if placeholder_type == "syarat_1":
            return random.choice(["form pengajuan", "surat tugas", "proposal kegiatan"])
        if placeholder_type == "syarat_2":
            return random.choice(["persetujuan ketua", "dokumentasi lengkap", "laporan evaluasi"])
        if placeholder_type == "waktu_proses":
            return str(random.randint(1, 7))
        return ""

    for i in range(start_id, start_id + num_entries):
        tipe_interaksi = random.choice(tipe_interaksi_options)
        current_topik = random.choice(tipe_interaksi_options)

        templates = interaction_templates[tipe_interaksi]
        template_pair = random.choice(templates)
        question = template_pair[0].replace("{topik}", current_topik)
        answer = template_pair[1].replace("{topik}", current_topik)

        for ph in ["departemen", "syarat_1", "syarat_2", "waktu_proses"]:
            placeholder = f"{{{ph}}}"
            if placeholder in question:
                question = question.replace(placeholder, get_random_placeholder(ph))
            if placeholder in answer:
                answer = answer.replace(placeholder, get_random_placeholder(ph))

        question = question.strip()
        answer = answer.strip()
        
        data.append({
            "tipe_interaksi": tipe_interaksi,
            "topik": current_topik,
            "question": question.strip(),
            "answer": answer.strip()
        })

    return data

jumlah=360000
data_kemahasiswaan = generate_chatbot_data(jumlah)

# Save to JSON
with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(data_kemahasiswaan, f, indent=2, ensure_ascii=False)

print(f"Dataset entri dataset.json berhasil dibuat.")