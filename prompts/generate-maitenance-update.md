Generate a maintenance closed PRs and issues report for the "<MILESTONE>"
milestone in ITISFoundation/osparc-simcore.

1. Use `gh` to search (don't scrape the GitHub web UI — it paginates/truncates).
2. Fetch closed PRs matching ANY of:
   - labels: `a:infra+ops`, `t:maintenance`, `e2e`
     (verify each label actually exists first with
     `gh label list --repo ITISFoundation/osparc-simcore` — fix typos, e.g.
     "t:mantenance" does not exist, the real label is "t:maintenance")
   - title keywords: `chore`, `dependencies`, `fix`, `maintenance`
   Query each label and each keyword SEPARATELY with `gh search prs` (repeated
   --label flags / a single query are ANDed, not ORed) and merge+dedupe the
   results by PR number in a script.
3. Fetch closed issues in the same milestone via `gh search issues --milestone
   <MILESTONE> --state closed`.
4. For each issue, find its resolving PR(s) via
   `gh api repos/<owner>/<repo>/issues/<n>/timeline --paginate -q
   '.[] | select(.event=="cross-referenced") | .source.issue |
   select(.pull_request != null) | "\(.number) \(.title)"'`
   then confirm each candidate PR is actually MERGED with `gh pr view <n>
   --json state,mergedAt`. Discard cross-referenced PRs that are clearly
   unrelated/old (e.g. from years-old refactors unrelated to this milestone).
5. Group PRs thematically based on their content — typical categories: Bug
   Fixes, Refactoring, Performance, Service Lifespan Migration, Observability /
   Tracing, Notifications & Emails, Frontend, E2E / Testing, Dependency
   Upgrades, CI / Tooling / Infra. Categorize using TITLE patterns, not labels
   — labels get applied broadly/automatically across unrelated PRs (e.g.
   almost every PR touching many services gets tagged with every a:xxx
   service label), so label-only categorization produces noisy results.
6. Group Issues thematically too (derive categories from the issues' actual
   subject matter, e.g. Computational Backend & Clusters, Storage & Rclone,
   Access Control, Products/Users & Groups, Notifications & Emails,
   Database & Dependency Upgrades, Release Management for pre-release/tracking
   issues). Format each as:
   ```
   - Issue: [#NNNN](url) title
     - Resolved by: [#NNNN](url) title @author
   ```
   (omit the "Resolved by" line entirely if no PR closed the issue).
7. Format each PR entry as: `- [#NNNN](url) title @author`.
8. Save as maintenance-prs-<milestone-slug>.md in the workspace root.
9. Ask me for a list of PR/issue numbers to highlight with a 👉 prefix
    (prepended before the `[#NNNN]` link), then apply it. If I'm unavailable to
    answer, skip highlighting rather than guessing.