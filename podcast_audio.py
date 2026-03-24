import asyncio
import edge_tts
import os

# --- CẤU HÌNH ---
VOICE = "vi-VN-HoaiMyNeural" 
OUTPUT_FOLDER = "content/audio"
RATE = "-30%" 
VOLUME = "+0%"
PITCH = "-20Hz"

async def generate_podcast(text, output_path):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, volume=VOLUME, pitch=PITCH)
    await communicate.save(output_path)
    print(f"\n✅ Đã 'nấu' xong Siêu phẩm Podcast tại: {output_path}")

def read_and_clean_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = []
        is_frontmatter = False
        for line in lines:
            if line.strip() == "---":
                is_frontmatter = not is_frontmatter
                continue
            if not is_frontmatter:
                content.append(line.strip())
        return " ".join(content)

async def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # ĐIỀN THƯ MỤC MÔN HỌC ÔNG MUỐN GOM (Ví dụ: Quản trị học)
    subject_folder = "content/03. Quản trị học" 
    
    # TÊN FILE MP3 ĐẦU RA
    output_mp3 = os.path.join(OUTPUT_FOLDER, "QuanTriHoc_Full_Podcast.mp3")

    full_text = ""
    count = 0

    print(f"🔍 Đang thu gom tài liệu từ lãnh địa: {subject_folder}...\n")
    
    # Vòng lặp quét toàn bộ file .md trong thư mục và các thư mục con
    for root, dirs, files in os.walk(subject_folder):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                text = read_and_clean_md(file_path)
                
                # Tách tên file để làm tiêu đề chuyển bài
                file_name_without_ext = file.replace(".md", "")
                
                # Nối chữ: Thêm câu báo hiệu chuyển bài để người nghe biết
                full_text += f". Chuyển sang phần: {file_name_without_ext}. " + text + " ... "
                
                count += 1
                print(f"  + Đã bòn rút thành công: {file}")

    if count > 0:
        print(f"\n🚀 Đã gom được {count} bài viết. Bắt đầu vận công bào chế Podcast...")
        print("⏳ (Có thể mất vài phút tùy vào độ dài của môn học, cứ lướt mạng chờ nhé!)")
        await generate_podcast(full_text, output_mp3)
    else:
        print("❌ Không tìm thấy file Markdown nào trong thư mục này!")

if __name__ == "__main__":
    asyncio.run(main())