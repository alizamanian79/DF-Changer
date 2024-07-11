import os

def replace_definer_and_export(input_file_path, output_file_path, old_definer, new_definer):
    # Check if the input file exists
    if not os.path.isfile(input_file_path):
        print(f"File '{input_file_path}' not found.")
        return

    # Read the contents of the SQL file
    with open(input_file_path, 'r') as file:
        content = file.read()

    # Replace the old definer with the new definer
    modified_content = content.replace(old_definer, new_definer)
    
    # Ensure the output folder exists
    output_folder = os.path.dirname(output_file_path)
    os.makedirs(output_folder, exist_ok=True)
    
    # Write the modified content to the new SQL file in the output path
    with open(output_file_path, 'w') as file:
        file.write(modified_content)
    
    print(f"Successfully replaced '{old_definer}' with '{new_definer}' and saved to '{output_file_path}'.")

# Get input paths from the user
input_file_path = input("Enter the full path to the input SQL file: ")
output_file_path = input("Enter the full path to the output SQL file: ")

oldDF=input("Old Definer: ")
old_definer = f"{oldDF}"
newDF=input("New Definer: ")
new_definer = f"{newDF}"

# Call the function to replace the definer and export the new file
replace_definer_and_export(input_file_path, output_file_path, old_definer, new_definer)
