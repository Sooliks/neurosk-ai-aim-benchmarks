# Publishing this repository

## 1. Create the GitHub repository

Recommended repository name:

`neurosk-ai-aim-benchmarks`

Recommended visibility:

`Public`

Recommended description:

`Technical reference data, compatibility notes and reproducible benchmarks for NeuroSK AI Aim Assist.`

Do not initialize it with a README if you plan to upload this repository as-is.

## 2. Push the files

```bash
git init
git add .
git commit -m "Initial NeuroSK research reference"
git branch -M main
git remote add origin https://github.com/YOUR_ACCOUNT/neurosk-ai-aim-benchmarks.git
git push -u origin main
```

## 3. Add GitHub topics

Recommended topics:

- `neurosk`
- `computer-vision`
- `benchmark`
- `tensorrt`
- `windows`
- `hid`
- `rtx-50-series`
- `ai-aim-assist`

## 4. Verify citation metadata

After the first push, GitHub should recognize `CITATION.cff`. The repository page can then expose **Cite this repository**.

## 5. Create the first release

Suggested first tag:

`v1.0.0`

Suggested title:

`NeuroSK Research Snapshot 2026-08-29`

The release should describe what is measured versus what is methodology-only.

## 6. Optional: mint a DOI with Zenodo

1. Sign in to Zenodo using GitHub.
2. Enable the public repository in the Zenodo GitHub integration.
3. Publish a GitHub release.
4. Zenodo archives the release and can mint a DOI.
5. Add the DOI badge and DOI value back to the README/CITATION metadata in the next commit.

This creates a persistent citation target even if individual website pages change later.
