---
description: Create deliverables (PPTX slides and Mermaid diagrams) based on the BricoLoc context, course evaluation criteria, and the professor's courses to ensure continuous improvement.
---
# Workflow: Generate Deliverables

This workflow generates high-quality deliverables such as slides for presentations and Mermaid architectural diagrams. It ensures that the generated content fully adheres to the requirements from the course (`08 - Cours/grille_évaluation.md`), the specific BricoLoc project context (`02-contexte/contexte-bricoloc.md`), and deeply embodies the intellectuality of the professor's teachings for continuous improvement.

## Prerequisites
- The agent must act as an IT architect planning outputs for the BricoLoc 2.0 project.
- The agent MUST embody the mindset, terminology, and expectations of the professor by leveraging the course materials.
- Deliverables must demonstrate a continuous improvement approach, constantly refining the existing architecture.
- All diagrams, outlines, and slides MUST be written in French.
- Use explicit visual cues, clean structures, and professional language.

## Step 1: Contextualization & Academic Alignment
Review the BricoLoc context and course materials to make sure the deliverables meet the highest expected standards. Always start by gathering information from relevant courses based on the topic at hand.

**Base Context to always review:**
- `02-contexte/contexte-bricoloc.md`
- `08 - Cours/grille_évaluation.md`

**Professor's Course Materials (Consult when relevant to accurately embody the course):**
- **TPs & Generalites:** `08 - Cours/INFAL235 - TP2 _ sujet.pdf`, `08 - Cours/INFAL235 - TP3 - sujet.pdf`, `08 - Cours/Partie 1 - Généralités.pdf`
- **Cloud Computing Foundations:** `08 - Cours/Partie 1 - émergence du cloud computing.pdf`, `08 - Cours/Partie 2 - notions, définitions et concepts du cloud computing.pdf`
- **Requirements & Strategy:** `08 - Cours/Partie 2 - Exigences.pdf`, `08 - Cours/Partie 5 - Stratégies d’utilisation du cloud computing.pdf`
- **Ecosystem & Providers:** `08 - Cours/Partie 3 - Les acteurs et les offres du cloud computing.pdf`
- **Architecture & Design:** `08 - Cours/Partie 3 - Modèles d'architecture.pdf`, `08 - Cours/Partie 4 - Représentations.pdf`, `08 - Cours/Partie 6 - Architectures Hors Normes.pdf`
- **Security & Choices:** `08 - Cours/Partie 4 - Les aspects juridiques, réglementaires et sécurité.pdf`, `08 - Cours/Partie 5 - Choix des technologies.pdf`

## Step 2: Goal Definition
Depending on the user's specific request, identify whether they need slides or diagrams (or both). Ask the user for specific parameters if not provided in the prompt (e.g., "What specific part of the architecture do you want to diagram?"). Filter which course PDFs are most relevant to this specific goal.

## Step 3: Diagram Generation (If applicable)
If creating Mermaid diagrams:
1. Ensure the architecture reflects the BricoLoc 2.0 vision (modern cloud-based, handling stock management, multi-warehouse logistics, etc.) and integrates lessons from the professor's architecture modules.
2. Use standard Mermaid syntax `flowchart TB` or `architecture`.
3. Apply styling rules to match existing documentation (e.g., using `%%` for section comments, grouping elements with `subgraph`, applying consistent color schemes using `style`). Reference `05-architecture/schema-infrastructure-ovh.md`.
4. Integrate the diagrams into markdown files with appropriate descriptions justifying architectural choices (use `Choix des technologies.pdf` and `Stratégies d'utilisation` for backing logic).

## Step 4: Slide Generation (If applicable)
If creating slides:
1. Provide a professional presentation outline adapted for an IT professional audience AND academic evaluation.
2. Structure the slide deck: Introduction, Context Breakdown, Architecture Logic, Justifications (with matrices), and Conclusion/Next Steps. Emphasize continuous improvement findings.
3. If requested, generate or modify python scripts (e.g., using `python-pptx`) to construct the `.pptx` file. Reuse existing Slide patterns found in `scripts/gen_pptx_part1.py` or `scripts/gen_pptx_part2.py`.

## Step 5: Final Review against Academic Standards
Check the deliverables against the evaluation grid (`08 - Cours/grille_évaluation.md`):
- Architecture schematics reflect all components and interactions (3 points).
- Logical structure justifies technology choices (2 points).
- The presentation format is professional and fluid (2 points).
- Verify that the academic rigor and "intellectuality" expected by the professor are unmistakably present in the tone and technical depth.
