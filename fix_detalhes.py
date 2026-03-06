import os
import re

template_dir = "c:/Users/Segurança/Documents/APP_FROTA/APP_FROTA/templates/APP_FROTA/"

def flatten_tag(match):
    inner = match.group(1)
    flat_inner = ' '.join(inner.split())
    return '{{ ' + flat_inner + ' }}'

def flatten_block(match):
    inner = match.group(1)
    flat_inner = ' '.join(inner.split())
    return '{% ' + flat_inner + ' %}'

files_to_fix = [f for f in os.listdir(template_dir) if f.endswith('.html')]

for filename in files_to_fix:
    file_path = os.path.join(template_dir, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Flatten variable tags {{ ... }}
    content = re.sub(r'\{\{([^}]+)\}\}', flatten_tag, content)
    
    # Flatten block tags {% ... %}
    content = re.sub(r'\{%([^%]+)%\}', flatten_block, content)

    # Special hack for file uploads in veiculo_detail.html if style is missing
    if filename == 'veiculo_detail.html' and "/* Hide clear checkbox container" not in content:
        style_to_add = """
    /* Hide clear checkbox container provided by django in readonly mode */
    .field-wrapper a {
        color: #00c6ff;
        text-decoration: none;
    }
    
    .field-wrapper br,
    .field-wrapper label[for$="-clear_id"] {
        display: none !important;
    }
    
    .field-wrapper input[type="file"] {
        display: none;
    }
    
    /* Reveal file inputs only when editing */
    .form-editing .field-wrapper input[type="file"] {
        display: block;
        margin-top: 10px;
    }
    
    /* Format the currently uploaded file string */
    .field-wrapper {
        font-size: 0.9rem;
    }
"""
        if '/* Style checkboxes specially */' in content:
            content = content.replace('/* Style checkboxes specially */', style_to_add + '\n    /* Style checkboxes specially */')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Sucesso! {len(files_to_fix)} templates foram corrigidos (tags achatadas).")
