import os

file_path = "c:/Users/Segurança/Documents/APP_FROTA/APP_FROTA/templates/APP_FROTA/veiculo_list.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to aggressively replace any lingering whitespace or multiline issues in the tag
content = content.replace("{{ veiculo.tipo_frota }}", "{{veiculo.tipo_frota}}")
content = content.replace("{{\n                        veiculo.tipo_frota }}", "{{veiculo.tipo_frota}}")
content = content.replace("{{\n veiculo.tipo_frota }}", "{{veiculo.tipo_frota}}")

# Just to be absolutely sure, let's explicitly inject the variable output
if "{{veiculo.tipo_frota}}" not in content and "{{ veiculo.tipo_frota }}" not in content:
    # If standard tags fail, we replace the whole line where the error could be
    import re
    content = re.sub(r'<span[^>]*style="background: rgba\(0, 150, 255, 0\.2\)[^>]*>.*?</span\s*>', 
                    '<span style="background: rgba(0, 150, 255, 0.2); padding: 4px 8px; border-radius: 12px; font-size: 0.85rem; border: 1px solid rgba(0, 150, 255, 0.4);">{{ veiculo.tipo_frota }}</span>',
                    content, flags=re.DOTALL)
    
    content = re.sub(r'<span[^>]*style="background: rgba\(138, 43, 226, 0\.2\)[^>]*>.*?</span\s*>', 
                    '<span style="background: rgba(138, 43, 226, 0.2); padding: 4px 8px; border-radius: 12px; font-size: 0.85rem; border: 1px solid rgba(138, 43, 226, 0.4);">{{ veiculo.tipo_frota }}</span>',
                    content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Script de correção HTML aplicado com sucesso!")
