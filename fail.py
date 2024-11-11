from tkinter import filedialog


def fail():
    global file_name
    file_name = filedialog.askopenfilename()

def count_lines_in_file():
    while True:
        try:
            fail()
            if len(file_name)==0 :
                print("file not chosen")
                break
            else:
                print("Chosen file:", file_name)

            # Ask for mode: text or binary
            mode = input("Do you want to open the file in text (t) or binary (b) mode? ").strip().lower()

            if mode == 't':
                mode = 'r'  
            elif mode == 'b':
                mode = 'rb'  
            else:
                print("Invalid mode selected. Please enter 't' for text or 'b' for binary.")
                continue

            # Try to open the file
            with open(file_name, mode) as file:
                # Check if file is in binary mode
                if 'b' in mode:
                    content = file.read()
                    line_count = content.count(b'\n')  
                else:
                    lines = file.readlines()
                    line_count = len(lines)  

                print(f"The file contains {line_count} lines.")
                break
        except UnicodeDecodeError:
            print("The file contains invalid characters.")
        except FileNotFoundError:
            print("Error: The file does not exist. Please try again.")
        except IOError:
            print("Error: The file cannot be read. Exiting the program.")
            break


if __name__ == "__main__":
    count_lines_in_file()
