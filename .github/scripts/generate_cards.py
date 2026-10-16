#!/usr/bin/env python3
"""
Generate Cyber-HPC Themed SVG Cards for CISSSCO README:
- Focus Areas (What I Build & What I Care About)
- Project Cards (OrgSlide, HPCCFS, playlisto, cerrfix, GitPush, CiscoRamon)
- Experience Cards (IIT BHU, C-DAC)

Exact content preserved from README.md, formatted in the unified Cyber-HPC aesthetic.
"""

import os
import html

OUTPUT_DIR = "assets/cards"

def wrap_text(text, max_len=48):
    words = text.split()
    lines = []
    curr = ""
    for w in words:
        if len(curr) + len(w) + 1 <= max_len:
            curr = (curr + " " + w).strip()
        else:
            if curr:
                lines.append(curr)
            curr = w
    if curr:
        lines.append(curr)
    return lines

def generate_focus_areas_svg(output_path):
    build_bullets = [
        "Distributed clusters, Slurm schedulers, and high-throughput environments",
        "MPI, OpenMP, CUDA, OpenACC, and SYCL parallel applications",
        "Spack upstream packaging and scientific software deployment",
        "Linux kernel & userland systems development, automation, and developer tooling",
        "Training environments and practical HPC benchmark testbeds",
    ]

    care_bullets = [
        "Scalable distributed research workloads and supercomputing systems",
        "Performance, latency, memory locality, and thoughtful systems design",
        "Reliable, reproducible, and automated Linux operating environments",
        "Active open-source contributions and maintainership",
        "Clear technical documentation and developer enablement",
    ]

    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 340" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1b2a"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
  </defs>

  <style>
    .mono { font-family: 'Fira Code', 'SF Mono', Consolas, Monaco, monospace; }
    .title { font-size: 13px; font-weight: 700; fill: #00f2fe; letter-spacing: 1px; }
    .card-title { font-size: 11px; font-weight: 700; letter-spacing: 0.8px; }
    .body-text { font-size: 11px; fill: #e5e7eb; }
  </style>

  <!-- Frame -->
  <rect width="880" height="340" rx="12" fill="url(#bgGrad)" stroke="#1e3a8a" stroke-width="1.5"/>

  <!-- Header -->
  <text x="32" y="34" class="mono title">
    &gt; TELEMETRY :: SPECIALIZATION &amp; CORE FOCUS DOMAINS
  </text>
  <line x1="32" y1="44" x2="848" y2="44" stroke="#1f2937" stroke-width="1"/>

  <!-- Left: What I Build -->
  <rect x="32" y="58" width="396" height="262" rx="8" fill="#111827" stroke="#1f2937" stroke-width="1"/>
  <rect x="46" y="70" width="144" height="24" rx="4" fill="#bd93f922" stroke="#bd93f9" stroke-width="1"/>
  <text x="118" y="86" class="mono card-title" fill="#bd93f9" text-anchor="middle">&#x26A1; WHAT I BUILD</text>
  <line x1="46" y1="104" x2="414" y2="104" stroke="#1f2937" stroke-width="0.8"/>
"""

    y_pos = 124
    for b in build_bullets:
        lines = wrap_text(b, 46)
        svg += f"""
  <g transform="translate(46, {y_pos})">
    <circle cx="6" cy="-4" r="3.5" fill="#00f2fe"/>
    <text x="18" y="0" class="mono body-text">{html.escape(lines[0])}</text>"""
        if len(lines) > 1:
            svg += f"""
    <text x="18" y="15" class="mono body-text">{html.escape(lines[1])}</text>"""
            y_pos += 36
        else:
            y_pos += 26
        svg += "\n  </g>"

    svg += """

  <!-- Right: What I Care About -->
  <rect x="452" y="58" width="396" height="262" rx="8" fill="#111827" stroke="#1f2937" stroke-width="1"/>
  <rect x="466" y="70" width="176" height="24" rx="4" fill="#00f2fe22" stroke="#00f2fe" stroke-width="1"/>
  <text x="554" y="86" class="mono card-title" fill="#00f2fe" text-anchor="middle">&#x1F52D; WHAT I CARE ABOUT</text>
  <line x1="466" y1="104" x2="834" y2="104" stroke="#1f2937" stroke-width="0.8"/>
"""

    y_pos = 124
    for b in care_bullets:
        lines = wrap_text(b, 46)
        svg += f"""
  <g transform="translate(466, {y_pos})">
    <circle cx="6" cy="-4" r="3.5" fill="#10b981"/>
    <text x="18" y="0" class="mono body-text">{html.escape(lines[0])}</text>"""
        if len(lines) > 1:
            svg += f"""
    <text x="18" y="15" class="mono body-text">{html.escape(lines[1])}</text>"""
            y_pos += 36
        else:
            y_pos += 26
        svg += "\n  </g>"

    svg += """
</svg>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

def generate_project_svg(project, output_path):
    title = project["title"]
    headline = project["headline"]
    description = project["description"]
    tags = project["tags"]

    head_lines = wrap_text(headline, 44)
    desc_lines = wrap_text(description, 50)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 215" width="100%" height="100%">
  <defs>
    <linearGradient id="pGrad_{title}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1b2a"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'SF Mono', Consolas, Monaco, monospace; }}
    .proj-title {{ font-size: 15px; font-weight: 700; fill: #00f2fe; letter-spacing: 0.5px; }}
    .badge-text {{ font-size: 9.5px; font-weight: 700; letter-spacing: 0.5px; }}
    .headline {{ font-size: 12.5px; font-weight: 600; fill: #ffffff; }}
    .desc {{ font-size: 11px; fill: #8b949e; line-height: 15px; }}
    .tag-text {{ font-size: 10px; font-weight: 600; }}
  </style>

  <!-- Frame -->
  <rect width="420" height="215" rx="10" fill="url(#pGrad_{title})" stroke="#1e3a8a" stroke-width="1.2"/>

  <!-- Top Bar -->
  <text x="18" y="27" class="mono" font-size="12" fill="#6e7681">~/projects/</text>
  <text x="105" y="27" class="mono proj-title">{html.escape(title)}</text>

  <!-- Repo Action Pill -->
  <rect x="338" y="14" width="64" height="18" rx="4" fill="#00f2fe18" stroke="#00f2fe" stroke-width="0.8"/>
  <text x="370" y="26" class="mono badge-text" fill="#00f2fe" text-anchor="middle">REPO &#x2197;</text>

  <line x1="18" y1="38" x2="402" y2="38" stroke="#1f2937" stroke-width="1"/>

  <!-- Headline -->
"""
    y_h = 58
    for hl in head_lines[:2]:
        svg += f"""  <text x="18" y="{y_h}" class="mono headline">{html.escape(hl)}</text>\n"""
        y_h += 16

    y_d = max(y_h + 8, 86)
    svg += """
  <!-- Description -->
"""
    for dl in desc_lines[:3]:
        svg += f"""  <text x="18" y="{y_d}" class="mono desc">{html.escape(dl)}</text>\n"""
        y_d += 16

    svg += """
  <!-- Tags -->
  <g transform="translate(18, 180)">
"""
    tag_x = 0
    for tag, color in tags:
        tag_w = len(tag) * 7.2 + 16
        svg += f"""    <rect x="{tag_x}" y="0" width="{tag_w:.1f}" height="20" rx="4" fill="{color}18" stroke="{color}" stroke-width="0.8"/>
    <text x="{tag_x + tag_w/2:.1f}" y="14" class="mono tag-text" fill="{color}" text-anchor="middle">{html.escape(tag)}</text>
"""
        tag_x += tag_w + 8

    svg += """  </g>
</svg>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

def generate_experience_svg(exp, output_path):
    role = exp["role"]
    role_color = exp.get("role_color", "#00f2fe")
    org = exp["org"]
    duration = exp["duration"]
    desc = exp["desc"]
    highlights = exp["highlights"]

    desc_lines = wrap_text(desc, 50)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 245" width="100%" height="100%">
  <defs>
    <linearGradient id="eGrad_{role[:4]}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0e17"/>
      <stop offset="50%" stop-color="#0d1b2a"/>
      <stop offset="100%" stop-color="#0a0e17"/>
    </linearGradient>
  </defs>

  <style>
    .mono {{ font-family: 'Fira Code', 'SF Mono', Consolas, Monaco, monospace; }}
    .badge-text {{ font-size: 10px; font-weight: 700; letter-spacing: 0.5px; }}
    .org-title {{ font-size: 12.5px; font-weight: 700; fill: #ffffff; }}
    .duration {{ font-size: 11px; font-weight: 500; fill: #38bdf8; }}
    .desc {{ font-size: 11px; fill: #9ca3af; line-height: 15px; }}
    .tag-text {{ font-size: 9.5px; font-weight: 600; }}
  </style>

  <!-- Frame -->
  <rect width="420" height="245" rx="10" fill="url(#eGrad_{role[:4]})" stroke="#1e3a8a" stroke-width="1.2"/>

  <!-- Top Bar: Role Badge -->
  <rect x="18" y="14" width="{len(role)*7.5 + 20:.1f}" height="22" rx="4" fill="{role_color}18" stroke="{role_color}" stroke-width="0.8"/>
  <text x="{18 + (len(role)*7.5 + 20)/2:.1f}" y="29" class="mono badge-text" fill="{role_color}" text-anchor="middle">{html.escape(role)}</text>

  <!-- Right Pill -->
  <rect x="306" y="14" width="96" height="22" rx="4" fill="#10b98118" stroke="#10b981" stroke-width="0.8"/>
  <text x="354" y="29" class="mono badge-text" fill="#10b981" text-anchor="middle">EXPERIENCE &#x2197;</text>

  <line x1="18" y1="44" x2="402" y2="44" stroke="#1f2937" stroke-width="1"/>

  <!-- Org & Duration -->
  <text x="18" y="66" class="mono org-title">{html.escape(org)}</text>
  <text x="18" y="84" class="mono duration">&gt; {html.escape(duration)}</text>

  <line x1="18" y1="94" x2="402" y2="94" stroke="#1f2937" stroke-width="0.8" stroke-dasharray="3,3"/>

  <!-- Description -->
"""
    y_d = 112
    for dl in desc_lines:
        svg += f"""  <text x="18" y="{y_d}" class="mono desc">{html.escape(dl)}</text>\n"""
        y_d += 16

    svg += """
  <!-- Highlights -->
  <g transform="translate(18, 210)">
"""
    tag_x = 0
    for tag, color in highlights:
        tag_w = len(tag) * 6.8 + 14
        svg += f"""    <rect x="{tag_x}" y="0" width="{tag_w:.1f}" height="20" rx="4" fill="{color}18" stroke="{color}" stroke-width="0.8"/>
    <text x="{tag_x + tag_w/2:.1f}" y="14" class="mono tag-text" fill="{color}" text-anchor="middle">{html.escape(tag)}</text>
"""
        tag_x += tag_w + 8

    svg += """  </g>
</svg>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated {output_path}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Focus Areas (What I Build & What I Care About)
    generate_focus_areas_svg(os.path.join(OUTPUT_DIR, "focus_areas.svg"))

    # 2. Projects (6 cards)
    projects = [
        {
            "title": "OrgSlide",
            "headline": "Turn Org-mode files into interactive web presentations.",
            "description": "A lightweight, zero-dependency client-side presentation engine for Emacs Org-mode with mindmap overviews and syntax highlighting.",
            "tags": [("Org-mode", "#bd93f9"), ("JavaScript", "#f1e05a"), ("Presentations", "#00f2fe")]
        },
        {
            "title": "HPCCFS",
            "headline": "Build an HPC cluster from scratch.",
            "description": "A practical path from bare hardware to a production-ready distributed high-performance compute environment.",
            "tags": [("HPC", "#bd93f9"), ("Linux", "#00f2fe"), ("Slurm", "#10b981")]
        },
        {
            "title": "playlisto",
            "headline": "Your Google Drive, turned into a music server.",
            "description": "A high-velocity personal streaming experience built around storage you already own.",
            "tags": [("Self-hosting", "#ff79c6"), ("Streaming", "#00f2fe"), ("TypeScript", "#3b82f6")]
        },
        {
            "title": "cerrfix",
            "headline": "Make Linux system errors actionable.",
            "description": "Rule-based diagnostics and remediation flows for system administration and runtime faults.",
            "tags": [("Automation", "#50fa7b"), ("CLI", "#00f2fe"), ("Linux", "#bd93f9")]
        },
        {
            "title": "GitPush",
            "headline": "Small command line, smoother Git workflow.",
            "description": "A minimal CLI that automates staging, commits, and upstream push sequences in one command.",
            "tags": [("Git", "#ff5555"), ("DevTools", "#3b82f6")]
        },
        {
            "title": "CiscoRamon",
            "headline": "Interactive 3D developer portfolio.",
            "description": "A React and Three.js immersive portfolio for presenting work, experiments, and technical interests.",
            "tags": [("React", "#00f2fe"), ("Three.js", "#ffffff")]
        },
    ]

    for p in projects:
        filename = f"project-{p['title'].lower()}.svg"
        generate_project_svg(p, os.path.join(OUTPUT_DIR, filename))

    # 3. Experiences (2 cards)
    experiences = [
        {
            "role": "HPC APPLICATION ENGINEER",
            "role_color": "#00f2fe",
            "org": "Indian Institute of Technology (BHU), Varanasi",
            "duration": "Feb 2025 — Aug 2026 · 1.5 Years",
            "desc": "Supporting scientific and research workloads on the PARAM Shivay supercomputing cluster (225+ nodes): cluster software stacks, job workflows, performance troubleshooting, and distributed Linux operations.",
            "highlights": [("PARAM Shivay (225+ Nodes)", "#00f2fe"), ("Slurm", "#3b82f6"), ("Cluster Ops", "#10b981")]
        },
        {
            "role": "PROJECT ENGINEER",
            "role_color": "#ff79c6",
            "org": "Centre for Development of Advanced Computing (C-DAC), India",
            "duration": "Apr 2024 — Present · 2.5 Years",
            "desc": "Contributing to the National Supercomputing Mission (NSM): HPC software R&D, SYCL & MPI case studies, parallel programming education, workshops, and technical mentoring.",
            "highlights": [("National Supercomputing Mission", "#ff79c6"), ("SYCL", "#00f2fe"), ("MPI", "#bd93f9")]
        }
    ]

    generate_experience_svg(experiences[0], os.path.join(OUTPUT_DIR, "experience-iitbhu.svg"))
    generate_experience_svg(experiences[1], os.path.join(OUTPUT_DIR, "experience-cdac.svg"))

    print("All cards generated successfully.")

if __name__ == "__main__":
    main()
