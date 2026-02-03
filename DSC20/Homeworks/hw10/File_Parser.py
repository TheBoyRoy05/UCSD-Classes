class File_Parser():
    def __init__(self, path):
        self.path = path
        self.info = {'ID': [], 'First Name': [], 'Last Name': []}
        
    def read_file(self):
        try:
            f = open(self.path, 'r')
            for line in f:
                indeces = ['ID', 'First Name', 'Last Name']
                line_info = line.strip().split(', ')
                if len(line_info) != 3:
                    raise ValueError('Invalid data format')
                for i in line_info:
                    self.info[indeces[i]] += [line_info[i]]
        except FileNotFoundError():
            print('File not found')
            
    def update_file(self, id, first_name, last_name):
        self.info['ID'] += [id]
        self.info['First Name'] += first_name
        self.info['Last Name'] += last_name