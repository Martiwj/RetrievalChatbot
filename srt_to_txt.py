def srt_to_txt(srt_file, txt_file):
    with open(srt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    subtitles = []
    for line in lines:
        # Sjekk om linjen inneholder tidspunkter eller andre metadata
        if '-->' in line or line.strip().isdigit() or 'Downloaded From' in line:
            continue
        elif line.strip() == '':
            continue
        else:
            subtitles.append(line.strip())
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(subtitles))

srt_to_txt('godfather.srt', 'god.txt')
