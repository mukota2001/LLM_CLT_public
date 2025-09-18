import os

# 指定ディレクトリ一覧（必要に応じて編集）
dirs = [
    "/data01/mukota/LLM_CLT/研究/figure/(66AM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(66PM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(67AM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(67PM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(68AM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(68PM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(69AM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(69PM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(71AM)臨床検査技師問題",
    "/data01/mukota/LLM_CLT/研究/figure/(71PM)臨床検査技師問題",
]

# 場合分けのしきい値（バイト単位）
HUGE = 20 * 1024 * 1024   # 20MB 以上
LARGE = 10 * 1024 * 1024  # 10MB 以上
MEDIUM = 5 * 1024 * 1024  # 5MB 以上

def analyze_dir(path: str) -> None:
    if not os.path.isdir(path):
        print(f"[WARN] ディレクトリが存在しません: {path}\n")
        return

    # pngファイルのみを対象
    png_files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(".png")]
    count = len(png_files)
    print(f"📂 {path}")
    print(f"  • 画像ファイル数: {count}")

    if count == 0:
        print("  （pngファイルがありません）\n")
        return

    # 最大サイズの取得
    max_file = max(png_files, key=lambda f: os.path.getsize(f))
    max_size = os.path.getsize(max_file)
    max_mb = max_size / (1024 * 1024)
    print(f"  • 最大サイズ: {max_mb:.2f} MB")
    print(f"  • 該当ファイル: {max_file}")

    # サイズによる場合分け
    if max_size >= HUGE:
        print("  → 判定: HUGE (20MB以上) : 解像度や圧縮率を見直してください")
    elif max_size >= LARGE:
        print("  → 判定: LARGE (10MB以上20MB未満) : 軽量化を推奨")
    elif max_size >= MEDIUM:
        print("  → 判定: MEDIUM (5MB以上10MB未満) : 配布用途に応じて検討")
    else:
        print("  → 判定: SMALL (5MB未満) : 特に対応不要")
    print()

def main():
    for d in dirs:
        analyze_dir(d)

if __name__ == "__main__":
    main()
