import os

# 🗂️ Danh sách các file chứa domain đã lưu về máy
input_files = [
    "/Users/ngocvuong/Documents/AdblockPlus.txt",
    "/Users/ngocvuong/Documents/oisd_nsfw_rpz.txt"
]

# ✅ Từ khóa liên quan đến nội dung Việt Nam hoặc người Việt thường tìm
vietnam_keywords = [
    'viet', 'vn', 'phim', 'truyen', 'vl',
    'sexgai', '' 'anhsex', 'xems', 'xemx',
    'xinh', 'dep', 'sexhay', 'sex-hay', 'cliphay', 'xhay' 'sexngon', 'sexmoi', 'clipmoi', 'suong', 'yeu', 'nung',
    'nhanh', 'lamtinh', 'nong', 'buom', 'gaigoi', 'checker', 'lauxanh', 'khongche',
    'conheo', 'loanluan', 'tinhcam', 'phang', 'noitieng', 'nguoi', 'nguoilon',
    'kieunu', 'phunu', 'congai', 'thudam', 'ngoaitinh', 'hocsinh', 'sinhvien',
    'mevo', 'chidau', 'nusinh', 'thempho', 'thiendia', 'giuong', 'chieu',
    'nhatban', 'trungquoc', 'nuocngoai', 'chaua', 'chaumy', 'chauau'
]

# ❌ Từ khóa cần loại bỏ (ví dụ: nội dung quốc tế không liên quan đến Việt Nam)
excluded_keywords = [
    'lond', 'lonl', 'lona',
    'depa','depe', 'depi', 'depr', 'depo', 'depu', 'deph',
    'hayden', 
    'enung',
    'prostitutki', 'voyeur'
]

# 🧹 Tập hợp domain duy nhất sau khi lọc
filtered_domains = set()

# 🔁 Đọc từng file và lọc domain hợp lệ
for file in input_files:
    if not os.path.exists(file):
        print(f"[!] Không tìm thấy file: {file}")
        continue
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            domain = line.strip().lower()
            if (
                domain and
                any(k in domain for k in vietnam_keywords) and
                not any(ex in domain for ex in excluded_keywords)
            ):
                filtered_domains.add(domain)

# 📝 Xuất kết quả
output_file = "vietnam_adult_filtered.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for domain in sorted(filtered_domains):
        f.write(domain + "\n")

print(f"✅ Đã lọc xong {len(filtered_domains)} domain → lưu tại '{output_file}'")