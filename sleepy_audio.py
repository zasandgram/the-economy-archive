import asyncio
import edge_tts
import os

# --- CẤU HÌNH ---
VOICE = "vi-VN-HoaiMyNeural" 
OUTPUT_FOLDER = "quartz/static/audio"
RATE = "-20%" 
VOLUME = "+0%"

async def generate_sleepy_audio(text, output_path):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, volume=VOLUME)
    await communicate.save(output_path)
    print(f"✅ Đã tạo xong file: {output_path}")

def read_markdown(file_path):
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

    # ĐƯỜNG DẪN FILE CỦA ÔNG (Tui đã chỉnh theo đúng cấu trúc folder của ông rồi đấy)
    input_md = "content/03. Quản trị học/Variebles/PDCA (Plan-Do-Check-Act).md" 
    output_mp3 = os.path.join(OUTPUT_FOLDER, "pdca_sleepy.mp3")

    if os.path.exists(input_md):
        text_to_read = read_markdown(input_md)
        print(f"🚀 Đang bào chế thuốc ngủ từ file: {input_md}")
        await generate_sleepy_audio(text_to_read, output_mp3)
    else:
        print(f"❌ Không tìm thấy file Markdown. Hãy check lại tên file trong code!")

if __name__ == "__main__":
    asyncio.run(main())