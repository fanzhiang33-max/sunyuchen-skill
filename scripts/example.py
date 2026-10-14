#!/usr/bin/env python3
"""输出一张离线每日成长卡片；不联网、不保存记录，也不主动推送。

运行示例：python example.py --minutes 20 --energy 3 --date 2026-10-14
面向技能维护者的命令行示例；日常对话由 SKILL.md 的流程负责。
"""

from __future__ import annotations

import argparse
from datetime import date


PLANS = (
    ("识别任务", "用 AI 拆解今天的一件真实任务，核验其中一个关键事实", "写下一个障碍，并列出两种可逆的解决办法"),
    ("保留成果", "用 AI 改写一份草稿，再标注哪些内容由你核实", "制作可展示的小成果：一段文字、一张草图或一个原型"),
    ("练习反馈", "请 AI 就当前学习主题出三道练习题，核对解析", "列出你感兴趣方向中的一个真实需求，并想一个访谈问题"),
    ("对照来源", "请 AI 总结一个公开资料，再检查原文是否支持结论", "比较两个职业或项目选项的成本、风险与可逆性"),
    ("缩小试验", "让 AI 把一件大任务分成今天可交付的一小步", "为一个方向设计不花钱或低成本的试验"),
    ("产出优先", "把本周学到的东西用 AI 辅助整理成自己的清单", "分享或存档一个有个人经验的可核验作品"),
    ("复盘与恢复", "复盘本周一个 AI 帮上忙和一个帮倒忙的案例", "写下下周继续、停止、尝试各一项"),
)


def main() -> None:
    parser = argparse.ArgumentParser(description="AI 化 · 健康化 · 未来化每日卡片")
    parser.add_argument("--minutes", type=int, choices=(5, 20, 45), default=5,
                        help="当日容量：5 / 20 / 45 分钟；默认 5 分钟")
    parser.add_argument("--energy", type=int, choices=range(1, 6), default=3,
                        metavar="1-5", help="精力评分；1-2 分自动降到 5 分钟版")
    parser.add_argument("--date", type=date.fromisoformat, default=date.today(),
                        help="按本地日期生成卡片，例如 2026-10-14")
    args = parser.parse_args()

    minutes = 5 if args.energy <= 2 else args.minutes
    theme, ai, future = PLANS[args.date.weekday()]
    if minutes == 5:
        ai = "用 AI 澄清一个小问题，并检查答案是否合理"
        health = "做一次适合自己的轻量活动或休息调整"
        future = "记下一条待验证的问题或机会"
        times = (2, 2, 1)
    elif minutes == 20:
        health = "做一段适合自己的活动或恢复；不适时改为休息"
        times = (7, 6, 7)
    else:
        health = "安排适合自己的活动、恢复或健康预约；遵循专业限制"
        times = (15, 15, 15)

    print(f"{args.date.isoformat()} · {theme} · {minutes} 分钟版")
    for title, task, duration in zip(("AI 化", "健康化", "未来化"),
                                     (ai, health, future), times):
        print(f"- {title}（约 {duration} 分钟）：{task}。完成证据：记一行结果。")
    print("今晚复盘：做了什么？哪里最难？明天继续、缩小、替换还是暂停？")
    print("按本人情况调整；重大健康、财务或职业判断不交给 AI 单独决定。")
    print("提示：这只生成卡片，不会自动定时提醒或保存隐私信息。")


if __name__ == "__main__":
    main()
