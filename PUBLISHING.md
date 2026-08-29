# Publishing this repository

## Current publication state

The public repository is live at:

`https://github.com/Sooliks/neurosk-ai-aim-benchmarks`

Zenodo integration is enabled and release `v1.0.1` is published with the permanent version DOI:

`10.5281/zenodo.22151633`

DOI resolver:

`https://doi.org/10.5281/zenodo.22151633`

## GitHub citation

`CITATION.cff` contains the current release version, DOI, and repository URL. GitHub can expose these values through **Cite this repository**.

## Publishing the next research snapshot

1. Update the research data, documentation, and source manifest.
2. Run the repository validator:

```bash
python scripts/validate_repository.py
```

3. Commit and push the changes to `main`.
4. Create a new GitHub release/tag such as `v1.0.2`.
5. Keep the release as a normal published release, not a draft or pre-release unless that is intentional.
6. Zenodo will archive the new GitHub release and mint a DOI for that exact snapshot.
7. Update `README.md` and `CITATION.cff` to reference the newly minted version DOI.

## DOI policy

The DOI currently stored in the repository is the **version DOI for `v1.0.1`**. Do not copy that DOI into `.zenodo.json` as if it identified future releases. Each future Zenodo archive receives its own version DOI.

If Zenodo exposes a separate concept DOI representing all versions of this repository, it can be added later as the preferred citation for the evolving project while keeping version DOIs for reproducible snapshot citations.

## Repository topics

Recommended GitHub topics:

- `neurosk`
- `computer-vision`
- `benchmark`
- `tensorrt`
- `windows`
- `hid`
- `rtx-50-series`
- `ai-aim-assist`
