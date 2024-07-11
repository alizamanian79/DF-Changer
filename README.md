
### README.md

#### Description
DF-Changer.py streamlines SQL file updates by replacing specified definers and exporting modified content. Designed for database procedures and functions, it facilitates seamless alterations during migrations or deployments, commonly replacing 'DEFINER=root@localhost' with user-specific details or any specified configuration.

#### How to Use
1. **Clone the Repository**
   ```
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Required Packages (if any)**
   ```
   # No additional packages required beyond standard Python libraries.
   ```

3. **Run the Script**
   - Navigate to the directory where `replace_definer_and_export.py` is located.
   - Execute the script using Python:
     ```
     python replace_definer_and_export.py
     ```

4. **Follow the Prompts**
   - You will be prompted to enter:
     - Full path to the input SQL file (`input_file_path`).
     - Full path to the output SQL file (`output_file_path`).
     - Old definer string (`old_definer`) to replace.
     - New definer string (`new_definer`) to replace with.

5. **Output**
   - The script will replace occurrences of `old_definer` with `new_definer` in the input SQL file.
   - It will then save the modified content to the specified output file (`output_file_path`).

6. **Error Handling**
   - If the input file (`input_file_path`) does not exist, an error message will be displayed.
   - The script ensures the output folder exists and creates it if necessary.

#### Example
Here’s an example of how to use the script:

```
Enter the full path to the input SQL file: /path/to/input_file.sql
Enter the full path to the output SQL file: /path/to/output_file.sql
Old Definer: 'DEFINER=root@localhost'
New Definer: 'DEFINER=admin@localhost'
Successfully replaced 'DEFINER=root@localhost' with 'DEFINER=admin@localhost' and saved to '/path/to/output_file.sql'.
```

#### Notes
- Ensure you have appropriate permissions to read from the input file and write to the output file.
- This script uses standard Python libraries (`os` and `open`), so no additional installations are required beyond Python itself.

#### Author
- Ali Zamanian

#### License
- No License.
