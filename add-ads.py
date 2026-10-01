# add-ads.py
# Terminal mein run karo: python add-ads.py
# Safe to run multiple times — skips files that already have ads

import os
import glob
import re

# ==========================================
# ADSTERRA CODES (Tumhare saare 10 codes)
# ==========================================

POPUNDER_CODE = """
<!-- Adsterra Popunder -->
<script data-cfasync="false" src="https://abscloud.org/1/45032587e7d7a35d9d75805f262c61b7"></script>
"""

SOCIAL_BAR_CODE = """
<!-- Adsterra Social Bar -->
<script data-cfasync="false" src="https://bauval.org/14/56d7c8a731fdc9252c3d18c4d8e5e404"></script>
"""

NATIVE_BANNER_CODE = """
<!-- Adsterra Native Banner -->
<script async="async" data-cfasync="false" src="https://bauval.org/21/1596516a27e033b01ae6393c71966508"></script>
<div id="container-1596516a27e033b01ae6393c71966508"></div>
"""

SMARTLINK_URL = "https://araplhn.org/4/6f633c11f78d7756dda09732542dac6e"

TOP_BANNER_728x90 = """
<!-- Adsterra Top Banner 728x90 -->
<div style="text-align:center; margin: 1.2rem 0; min-height: 90px;">
<script>
  atOptions = {
    'key' : '538dc06ae7c6515acaa5b97ebdb5ceaa',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/538dc06ae7c6515acaa5b97ebdb5ceaa"></script>
</div>
"""

CALC_RESULT_BANNER_300x250 = """
<!-- Adsterra Calculator Result Banner 300x250 -->
<div style="text-align:center; margin: 1.5rem 0; min-height: 250px;">
<script>
  atOptions = {
    'key' : '127be41a6b922a8dc7882d6b2e226a24',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/127be41a6b922a8dc7882d6b2e226a24"></script>
</div>
"""

ARTICLE_MIDDLE_BANNER_468x60 = """
<!-- Adsterra Article Middle Banner 468x60 -->
<div style="text-align:center; margin: 1.5rem 0; min-height: 60px;">
<script>
  atOptions = {
    'key' : 'ead2c23e3ff45d88fe3c3323de834816',
    'format' : 'iframe',
    'height' : 60,
    'width' : 468,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/ead2c23e3ff45d88fe3c3323de834816"></script>
</div>
"""

# ==========================================
# SCRIPT LOGIC (Ise change mat karo)
# ==========================================

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def add_site_wide_ads(file_path):
    """Popunder + Social Bar + Native Banner daalta hai </body> se pehle."""
    content = read_file(file_path)

    if '<!-- Adsterra Popunder -->' in content:
        print(f"  SKIP: {file_path} (site-wide ads already added)")
        return

    ad_block = POPUNDER_CODE + SOCIAL_BAR_CODE + NATIVE_BANNER_CODE
    if '</body>' in content:
        content = content.replace('</body>', ad_block + '\n</body>')
        write_file(file_path, content)
        print(f"  DONE: {file_path} (site-wide ads added)")
    else:
        print(f"  WARN: {file_path} (no </body> tag)")

def add_top_banner(file_path):
    """Top banner breadcrumb ke baad daalta hai."""
    content = read_file(file_path)

    if '<!-- Adsterra Top Banner 728x90 -->' in content:
        print(f"  SKIP: {file_path} (top banner already added)")
        return

    # Breadcrumb ke closing </div> ke baad daalo
    pattern = r'(<div class="breadcrumb">.*?</div>\s*)(\n\s*<(?:section|article))'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        insert_after = match.end(1)
        content = content[:insert_after] + '\n' + TOP_BANNER_728x90 + content[insert_after:]
        write_file(file_path, content)
        print(f"  DONE: {file_path} (top banner added)")
    else:
        print(f"  WARN: {file_path} (breadcrumb pattern not found for top banner)")

def add_calc_result_banner(file_path):
    """Calculator result ke baad 300x250 banner daalta hai."""
    content = read_file(file_path)

    if '<!-- Adsterra Calculator Result Banner 300x250 -->' in content:
        print(f"  SKIP: {file_path} (calc banner already added)")
        return

    start_idx = content.find('<div class="card" id="calcContainer">')
    if start_idx == -1:
        print(f"  WARN: {file_path} (calcContainer not found)")
        return

    next_section = content.find('<section class="content"', start_idx)
    if next_section == -1:
        next_section = content.find('</main>', start_idx)

    if next_section == -1:
        print(f"  WARN: {file_path} (cannot find insertion point for calc banner)")
        return

    content = content[:next_section] + '\n' + CALC_RESULT_BANNER_300x250 + '\n' + content[next_section:]
    write_file(file_path, content)
    print(f"  DONE: {file_path} (calc result banner added)")

def add_article_middle_banner(file_path):
    """Article ke beech mein 468x60 banner daalta hai."""
    content = read_file(file_path)

    if '<!-- Adsterra Article Middle Banner 468x60 -->' in content:
        print(f"  SKIP: {file_path} (article banner already added)")
        return

    # Pehle <h2> ke baad daalo
    pattern = r'(<h2>.*?</h2>\s*)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        insert_after = match.end(1)
        content = content[:insert_after] + '\n' + ARTICLE_MIDDLE_BANNER_468x60 + content[insert_after:]
        write_file(file_path, content)
        print(f"  DONE: {file_path} (article middle banner added)")
    else:
        print(f"  WARN: {file_path} (no <h2> found for article banner)")

def add_smartlink_to_home(file_path):
    """Homepage footer mein smartlink add karta hai."""
    content = read_file(file_path)

    if SMARTLINK_URL in content:
        print(f"  SKIP: {file_path} (smartlink already added)")
        return

    pattern = r'(<a href="/privacy">Privacy</a> \|)'
    match = re.search(pattern, content)

    if match:
        new_link = f' <a href="{SMARTLINK_URL}" target="_blank" rel="noopener">Recommended Tools</a> |'
        content = content.replace(match.group(1), match.group(1) + new_link)
        write_file(file_path, content)
        print(f"  DONE: {file_path} (smartlink added to footer)")
    else:
        print(f"  WARN: {file_path} (footer pattern not found for smartlink)")

def main():
    print("=" * 60)
    print("  Calqin.com Ad Placement Script")
    print("=" * 60)

    html_files = glob.glob('**/*.html', recursive=True)
    if not html_files:
        print("\n❌ Koi HTML file nahi mili. Sahi folder mein run karo.")
        return

    print(f"\n📁 Total {len(html_files)} HTML files mili.\n")

    # Step 1: Har file par site-wide ads
    print("--- Step 1: Site-wide Ads (Popunder + Social Bar + Native) ---")
    for file_path in html_files:
        add_site_wide_ads(file_path)

    # Step 2: Top Banner har page par
    print("\n--- Step 2: Top Banner (728x90) ---")
    for file_path in html_files:
        add_top_banner(file_path)

    # Step 3: Calculator result banner
    print("\n--- Step 3: Calculator Result Banner (300x250) ---")
    calculator_files = [f for f in html_files if 'calculators' in f.replace('\\', '/')]
    for file_path in calculator_files:
        add_calc_result_banner(file_path)

    # Step 4: Article middle banner
    print("\n--- Step 4: Article Middle Banner (468x60) ---")
    blog_articles = [f for f in html_files if 'blog' in f.replace('\\', '/').lower() and 'index' not in os.path.basename(f).lower()]
    for file_path in blog_articles:
        add_article_middle_banner(file_path)

    # Step 5: Smartlink homepage footer mein
    print("\n--- Step 5: Smartlink in Footer ---")
    home_files = [f for f in html_files if os.path.basename(f) == 'index.html' and os.path.dirname(f) == '.']
    for file_path in home_files:
        add_smartlink_to_home(file_path)

    print("\n" + "=" * 60)
    print("  ✅ Process Complete!")
    print("=" * 60)
    print("\n📌 Next Steps:")
    print("  1. Apni website browser mein kholo (Incognito mode)")
    print("  2. Ads check karo (AdBlock off rakho)")
    print("  3. git add .")
    print("  4. git commit -m 'Add Adsterra ads'")
    print("  5. git push")
    print()

if __name__ == "__main__":
    main()