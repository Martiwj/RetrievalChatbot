def csv_to_txt(csv_file, txt_file):
    
    with open(csv_file, "r", encoding="utf-8") as f:
        with open(txt_file, "w", encoding="utf-8") as new_filename:
            symbol_to_trim = '"'
            sm = '"'
            lines = f.readlines()
        
            for line in lines:
                line_to_write = line.split(",")[5].strip(symbol_to_trim).rstrip(sm)
                new_filename.write(line_to_write)

