EXAMPLE = {
    1 : {
        363517227535826958:"their_embed",
        123456789123456789:"their_embed"
        },
    
    2 : {
        746209701804507136:"their_embed",
        987654321987654321:"their_embed"
        }
}


class NestedHashMapError(Exception):
    pass


# make bot @mention scrim role and create a scrim role
# make bot command that sets scrim role
class NestedHashMap:
    def __init__(self, structure: dict = {}):
        self.overwrite(structure)


    def __iter__(self):
        for outer_key, inner_dictionary in self.structure.items():
            if not bool(inner_dictionary):
                yield outer_key, None, None
            else:
                for inner_key, inner_value in inner_dictionary.items():
                    yield outer_key, inner_key, inner_value


    # add more operator overloards like adding or comparing
    def __str__(self):
        return f'{self.structure}'


    def display(self):
        open_brace, close_brace = '{','}'
        for ok, ov in self.structure.items():
            print(f'{ok} : {open_brace}')
            for ik, iv in ov.items():
                if len(ov) <= 1:
                    print(f'{open_brace}{ik} : {iv}{close_brace}')
                else:
                    print(f'{open_brace}{ik} : {iv}{close_brace},')
            print(f'{close_brace}\n----------')


    def update_server_count(self) -> None:
        # on_server_join
        # on_server_leave
        self.server_count = len(self.structure)

    def add(self, key, value = {}) -> bool:
        '''Adds a new key row to the NestedHashMap with the corresponding value.
        If no valid value is specified, then a empty dictionary will be added at that key.'''
        # on_server_join
        # on_member_join
        # existing member used a command
        if key in self.structure:
            return None
        elif not isinstance(value, dict):
            self.structure[key] = {}
            self.update_server_count()
            print('value was not a dict')
        else:
            self.structure[key] = value
            self.update_server_count()
        return True


    def remove(self, key) -> bool:
        # on_server_leave
        # on_member_leave
        # whenever a user deletes a post
        # every 3 days when posta re auto deleted, remove all users 
        try:
            del self.structure[key]
            return True
        except:
            return False


    def set(self, key, value: dict) -> bool:
        # when a user creates a post and they already have an outstanding one
        if type(value) == dict and not self.structure[key]:
            self.structure[key] = value
            return True
        return False


    def clear(self) -> None:
        '''Removes all entries from the called NestedHashMap object'''
        self.structure = {}
        self.server_count = 0


    def overwrite(self, NEW_NHM: object = {}) -> bool:
        '''Takes in a NestedHashMap object or a dictionary object.
        Sets the called NestedHashMap object to the given arguement.
        Returns True

        If any other type of arguement was provided or None, then the called NestedHashMap object is cleared.
        Returns False'''

        if isinstance(NEW_NHM, NestedHashMap):
            self.structure = NEW_NHM.structure
            self.update_server_count()
            return True
        elif isinstance(NEW_NHM, dict):
            self.structure = NEW_NHM
            self.update_server_count()
            return True
        self.clear()
        return False


    def process_query(self, query: str):
        pass


# create a method that handles reading queries each word being separated by 1 space
    def QUERY(self, query: str = 'SELECT') -> bool | object: # return True if processed or False if not/error
        # return the selected object if select was used
        if not isinstance(query, str):
            return False
        if query == 'SELECT':
            return self.structure


# TODO QUERY COMMANDS (use custom error class when inputting invalid query), 
# PROTOdatabase.query("DROP TABLE <primary_key>")
PROTOdatabase = NestedHashMap(EXAMPLE)

PROTOdatabase.add(3,{12:'test'})

PROTOdatabase.add(7)

PROTOdatabase.display()

print(PROTOdatabase)

for o,i,v in PROTOdatabase:
    print(o,i,v)
