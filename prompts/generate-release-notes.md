# Release Notes Generation Prompt

## Purpose

This prompt will help you generate comprehensive, well-structured release notes from a list of commit messages and PR links.

## Instructions

Given a list of commit messages under "What's Changed" section with PR links:

1. Analyze each commit message and its associated PR link.
2. Group related changes by functional area (e.g., Frontend, public API, Performance, Security, User Management, etc.).
3. For each functional area:
   - Create a concise summary bullet point that explains the changes in user-friendly language
   - Focus on the benefit to users rather than technical implementation
   - Include PR link references in parentheses at the end of relevant points
   - Avoid mentioning specific developer names in the summary

4. Prioritize highlighting:
   - New features (✨)
   - Bug fixes (🐛)
   - Performance improvements (🎨, ♻️)
   - Security enhancements (🔒)
   - Breaking changes (⚠️, 🚨)

5. Format the output as follows:

   ```markdown
   ### Highlights

   - **[Functional Area 1]**: Concise description of major changes and their benefits to users ([#PR-number](PR-link))

   - **[Functional Area 2]**: Concise description of major changes and their benefits to users ([#PR-number](PR-link), [#PR-number](PR-link))

   <details>
   <summary>Show detailed release notes</summary>

   ## What's Changed
   [Original commit messages with PR links]
   </details>
   ```

6. Ensure the highlights section is readable by non-technical users and focuses on the "what" and "why" rather than the "how".

7. For significant changes, consider adding a brief explanation of how to use new features or migrate from previous behavior.

## Example

For a commit message like:
* 🎨 web-server: accelerate `input:match` via caching rest client call by @pcrespov in https://github.com/ITISFoundation/osparc-simcore/pull/7802

The highlight might be:
- **Performance Improvements**: Accelerated port compatibility checks through REST client call caching for faster response times ([#7802](https://github.com/ITISFoundation/osparc-simcore/pull/7802))
