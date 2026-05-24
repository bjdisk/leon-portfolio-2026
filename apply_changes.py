#!/usr/bin/env python3
"""Apply all changes from v2.3 spec to index.html"""

import re

with open('/home/user/leon-portfolio-2026/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ============================================================
# [B1-B5] Hero section — check and fix labels (already done)
# These were already applied. Verify and skip if correct.
# The file already has the new text based on reading.
# ============================================================
# The hero section already has the correct text per the read.

# ============================================================
# [C1] Twitch — Challenge Chinese
# ============================================================
content = content.replace(
    '必須在極度緊湊的時間窗口內，交付零延遲、高規格的星光大道接駁與現場試駕服務。',
    '必須在極度緊湊的時間窗口內，交付高效率、高規格的星光大道接駁與現場試駕服務。'
)

# ============================================================
# [C2] Twitch — Strategy Chinese
# ============================================================
content = content.replace(
    '強力護航頂級利害關係人的極致體驗',
    '確保頂級利害關係人的全程體驗不受干擾'
)

# ============================================================
# [C3] Twitch — Impact header (check if already done)
# ============================================================
# File already shows 影響與交付 in Twitch section — skip

# ============================================================
# [C4+C5] Twitch — Impact body
# ============================================================
content = content.replace(
    '寫下單車每小時運轉 10 趟的極限效率，將高風險現場轉化為毫無摩擦的品牌完美觸達。',
    '單車維持每小時 10 趟的峰值運轉效率，將高風險公共場域收斂為流暢、可控的品牌體驗觸點。'
)
# EN version already correct per the read — keep it

# ============================================================
# [C6] BMW X3 — Metric label
# ============================================================
content = content.replace(
    '筆高資產 CRM 紀錄</span><span class="lang-en">High-Net-Worth CRM Records</span>',
    '筆 VIP CRM 紀錄</span><span class="lang-en">VIP CRM Records</span>'
)

# ============================================================
# [C7] BMW X3 — Challenge Chinese (already done per read)
# ============================================================
# Already shows new text — skip

# ============================================================
# [C8-C10] BMW X3 — Impact (already done per read)
# ============================================================
# Already shows 影響與轉換 and new body — skip

# ============================================================
# [C11-C12] GEN M — Challenge (already done per read)
# ============================================================
# Already shows new text — skip

# ============================================================
# [C13-C14] GEN M — Strategy
# ============================================================
content = content.replace(
    '確保奢華體驗不中斷。',
    '確保品牌體驗的連貫性不受波及。'
)
content = content.replace(
    'keep the luxury experience uninterrupted.',
    'keep the brand experience uninterrupted.'
)

# ============================================================
# [C15-C17] GEN M — Impact (already done per read)
# ============================================================
# Already shows 影響與沉澱 and new body — skip

# ============================================================
# [D1] Professional Matrix — Language fix for Workflow Automation
# ============================================================
content = content.replace(
    '<div class="py-3 text-[12px] text-slate-400 font-mono tracking-wider">Workflow Automation</div>',
    '<div class="py-3 text-[12px] text-slate-400 font-mono tracking-wider"><span class="lang-zh">AI 工作流整合</span><span class="lang-en">Workflow Automation</span></div>'
)

# ============================================================
# [E1] Career Timeline — Insert BMW 2022-至今 entry BEFORE Wah Hou
# ============================================================
wah_hou_entry = '''                <div class="p-5 bg-slate-900/40 border border-slate-700/50 rounded-lg">
                    <span class="text-[11px] font-mono text-slate-500">2017 - 2022</span>'''

bmw_entry = '''                <div class="p-5 bg-slate-900/40 border border-slate-700/50 rounded-lg">
                    <span class="text-[11px] font-mono text-slate-500">2022 - 至今</span>
                    <h3 class="text-base font-bold text-slate-100 mt-0.5"><span class="lang-zh">汎德永業汽車股份有限公司汎德台北分公司 // 行銷專員</span><span class="lang-en">Pan German Motors (BMW Taipei Pan German) — Marketing Professional</span></h3>
                    <p class="text-sm text-slate-400 mt-3 leading-relaxed font-sans tracking-wide">
                        <span class="lang-zh">統籌 BMW 品牌在台灣市場的整合行銷活動與專案交付。主責新車上市發表、車主體驗活動與跨通路品牌執行，並導入 AI 工作流強化內部規劃效率與數據追蹤精度。</span><span class="lang-en">Leads integrated marketing campaigns and end-to-end project delivery for BMW in Taiwan. Core responsibilities span new model launches, owner experience programs, and cross-channel brand execution — with AI-augmented workflows integrated into planning and tracking processes.</span>
                    </p>
                </div>
''' + wah_hou_entry

content = content.replace(wah_hou_entry, bmw_entry, 1)

# ============================================================
# [E2] Wah Hou — Append sentence (already done per read)
# The file already has 任內與 Poly、Genesys、Logitech 等一線科技品牌建立長期協作默契。
# ============================================================

# ============================================================
# [A1] CHANGELOG — Collapsible accordion
# ============================================================
# The current CHANGELOG section:
old_changelog_section = '''        <section class="fade-in-up pt-8 border-t border-slate-700/50">
            <h2 class="text-[11px] font-bold tracking-[0.4em] text-slate-500 uppercase mb-6 font-mono">
                // SYSTEM_DESIGN_CHANGELOG (PDCA_LOOP)
            </h2>
            <div class="space-y-4 font-mono text-[12px] text-slate-500 leading-relaxed">'''

new_changelog_section = '''        <section class="fade-in-up pt-8 border-t border-slate-700/50">
            <button id="changelogToggle" class="w-full text-left flex items-center justify-between text-[11px] font-bold tracking-[0.4em] text-slate-500 uppercase border-b border-slate-700/50 pb-3 font-mono cursor-pointer hover:text-slate-400 transition-colors">
                <span>// SYSTEM_DESIGN_CHANGELOG (PDCA_LOOP)</span>
                <span class="text-base tracking-normal transition-transform duration-300" id="changelogChevron">▼</span>
            </button>
            <div id="changelogBody" class="overflow-hidden transition-[max-height] duration-300 ease-in-out" style="max-height: 0;">
            <div class="space-y-4 font-mono text-[12px] text-slate-500 leading-relaxed">'''

content = content.replace(old_changelog_section, new_changelog_section, 1)

# Close the changelog body div — find the end of the changelog section
# The section ends with:   </div>            </div>\n        </section>
old_changelog_end = '''            </div>            </div>
        </section>

    </main>'''

new_changelog_end = '''            </div>
            </div>
            </div>
        </section>

    </main>'''

content = content.replace(old_changelog_end, new_changelog_end, 1)

# ============================================================
# [F] Portrait Section — Insert after Career Timeline, before footer
# ============================================================
# The career timeline section closes before </main>
# After applying the above, </main> follows the changelog section closing
# We need to insert the portrait section before </main>

portrait_section = '''
        <section class="fade-in-up">
            <div class="relative z-10 bg-neutral-950/40 backdrop-blur-xl border border-white/[0.06] shadow-2xl shadow-black/60 rounded-2xl p-6 md:p-10">
            <h2 class="text-[11px] font-bold tracking-[0.4em] text-slate-500 uppercase border-b border-slate-700/50 pb-3 font-mono mb-8">
                <span class="lang-zh">// THE PERSON // 關於這個人</span><span class="lang-en">// THE PERSON // About</span>
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-5 gap-8 md:gap-12 items-start">
                <!-- Portrait photo -->
                <div class="md:col-span-2">
                    <!-- Replace with actual portrait photo -->
                    <div class="overflow-hidden rounded-[12px] border border-slate-700/50">
                        <img id="portrait-photo"
                             src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&h=800&fit=crop&q=80&auto=format"
                             alt="Leon Chu"
                             class="w-full aspect-[3/4] object-cover grayscale opacity-60 hover:grayscale-0 hover:opacity-100 transition-all duration-500"/>
                    </div>
                </div>
                <!-- Personal statement + contact -->
                <div class="md:col-span-3 space-y-6">
                    <div class="text-sm text-slate-400 leading-relaxed font-sans tracking-wide space-y-4">
                        <p class="lang-zh">我相信每一場活動背後，都藏著一個讓人想留下來的理由。<br>心理學訓練讓我習慣先問「為什麼」，行銷實務讓我知道怎麼把答案變成現場裡真實發生的事。<br>十年下來，我最記得的不是那些數字，而是把一件困難的事做對的那個過程。</p>
                        <p class="lang-en">Behind every event is a reason people choose to stay.<br>Psychology taught me to ask why first. Marketing taught me to turn that answer into something that happens in the room.<br>A decade in — what I remember most isn't the numbers. It's the process of getting a hard thing right.</p>
                    </div>
                    <div class="pt-5 border-t border-slate-700/50 space-y-2">
                        <div class="flex items-center gap-3 text-[12px] text-slate-400 font-mono">
                            <span class="text-slate-500 shrink-0">TEL</span>
                            <span>+886 903-817761</span>
                        </div>
                        <div class="flex items-center gap-3 text-[12px] text-slate-400 font-mono">
                            <span class="text-slate-500 shrink-0">MAIL</span>
                            <span>bjdisklol@gmail.com</span>
                        </div>
                        <div class="flex items-center gap-3 text-[12px] text-slate-400 font-mono">
                            <span class="text-slate-500 shrink-0">LOC</span>
                            <span>Taipei, Taiwan</span>
                        </div>
                    </div>
                </div>
            </div>
            </div>
        </section>'''

content = content.replace('\n    </main>', portrait_section + '\n\n    </main>', 1)

# ============================================================
# [A1] Add JS for changelog accordion — before </script>
# ============================================================
js_changelog = '''
        // 3. Changelog accordion toggle
        const changelogToggle = document.getElementById('changelogToggle');
        const changelogBody = document.getElementById('changelogBody');
        const changelogChevron = document.getElementById('changelogChevron');
        changelogToggle.addEventListener('click', () => {
            const isOpen = changelogBody.style.maxHeight !== '0px' && changelogBody.style.maxHeight !== '';
            if (isOpen) {
                changelogBody.style.maxHeight = '0';
                changelogChevron.style.transform = 'rotate(0deg)';
            } else {
                changelogBody.style.maxHeight = changelogBody.scrollHeight + 'px';
                changelogChevron.style.transform = 'rotate(180deg)';
            }
        });
'''

# The existing comment "// 2. Timeline 常態顯示..." needs to be renumbered
# but we just add a new section. The existing script has numbered comments.
# Instructions say add before </script>
content = content.replace('    </script>\n</body>', js_changelog + '    </script>\n</body>', 1)

# Write the modified content
with open('/home/user/leon-portfolio-2026/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("All changes applied successfully.")
print(f"Original length: {len(original)}")
print(f"New length: {len(content)}")
print(f"Difference: {len(content) - len(original)} chars added")
