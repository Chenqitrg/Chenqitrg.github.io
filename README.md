# Chenqi Meng's academic website

Public site: https://chenqitrg.github.io/

A responsive English academic homepage. Static HTML and CSS, with no build step, external font service, JavaScript dependency, or analytics.

## Editorial style

Keep the presentation understated and factual. Use plain section headings and standard publication entries with full coauthor credit. Mention collaborative software briefly, without implying sole ownership. Keep BoundaryBulkKit to a secondary code link rather than a featured project.

## Editing

- `index.html`: biography, research, publications, software, education, and contact information.
- `styles.css`: typography, colors, spacing, mobile layout, and print styles.
- `assets/chenqi-meng.jpg`: portrait from the public CUHK profile, used at the owner's request.
- `assets/chenqi-meng-cv.pdf`: current downloadable CV.
- `scripts/build_cv.py`: editable CV content and PDF generation. Install `reportlab`, then run `python3 scripts/build_cv.py`.
- `assets/publications.bib`: downloadable bibliography.

When adding a publication, update the homepage, bibliography, and CV script, regenerate the PDF, and update the visible revision date and sitemap. Check journal status against the publisher or arXiv; do not label a preprint as a published article.

## Preview

Run `python3 -m http.server 8000 --bind 127.0.0.1` from this directory and open http://127.0.0.1:8000/.

## Hosting

GitHub Pages serves the root directory of the default branch. Push changes to that branch to update the website. `.nojekyll` disables Jekyll processing. No custom domain or paid hosting is required.

## Content sources

Verified on 21 October 2026:

- Owner-provided CV for education, skills, interests, and contact details.
- [CUHK profile](https://app.phy.cuhk.edu.hk/postgraduates/meng-chenqi/) for affiliation, advisor, education, and portrait.
- [Algebraic TNR preprint](https://arxiv.org/abs/2610.08787).
- [TNRKit paper and journal reference](https://arxiv.org/abs/2604.06922), SciPost Physics Codebases 77 (2026), DOI: 10.21468/SciPostPhysCodeb.77.
- [Non-invertible SPTs preprint](https://arxiv.org/abs/2412.20546).
- [TNRKit repository](https://github.com/QuantumKitHub/TNRKit.jl).
- [BoundaryBulkKit repository](https://github.com/Chenqitrg/BoundaryBulkKit.jl).

The website CV adds the October 2026 preprint, corrects TNRKit's publication status and author order, and updates the revision date. The original personal CV files are not part of this repository. No expected graduation date or postdoctoral availability date is assumed.
