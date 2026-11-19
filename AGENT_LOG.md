# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-19: City median sale price chart and table

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then add a horizontal bar chart of the median shale price for each city above the table on index.html. Keep the table and the $10,000 rule as they are." Then: "There's no table yet. Please add both: a table of each city's sales count and median sale price, and the horizontal bar chart of median sale price above it. [...] Yes, the $10,000 rule means leave out sales under $10,000 (and blank prices). State the rule on the page, with how many sales it removed. Keep it on the branch and open a pull request into main."
- **Agent produced:** `scripts/city_median_prices.py`, which writes `data/city_median_sale_prices.json` (sales count and median per city, plus the rule and the counts removed). `index.html` now shows the rule, a horizontal bar chart, and a table, all drawn from that JSON. Result: 35,442 rows; 40 left out under $10,000; none blank; 35,402 used in 18 cities.
- **Checked or changed:** The agent rendered the page in a headless browser at 375 px and 1200 px wide. It found no sideways scrolling and no script errors, and it found 18 bars and 18 table rows. It also fixed two problems it saw in a phone screenshot: value labels overlapping short bars, and a half-dollar median showing one decimal place. Not yet checked by you.
