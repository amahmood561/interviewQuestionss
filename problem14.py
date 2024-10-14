'''
Software version are stores as a string whuch has 5 parts. stored as a the format [major].[minor].[patch].[build].[compilation]. each version part will always be  non-negative integer. you may see versions like "2". The period is only used as a seperator and does not represent a decimal point(i.e 1.5 does no mean one and a half) 

algorith mdetails 

you algorithm should have two string input paramers : version1 and version2. it should return -1 when version1 is less than version 2 , 0 when version1 == version2 and 1 when version1 is greater than version2 .

examples 

"2" == "2.0" == "2.0.0" == "2.0.0.0" == "2.0.0.0.0"returns 0

"2" < "2.0.0.0.1" returns -1 
"2" < "2.1" returns -1 
"2.1.0"  > "2.0.1" returns 1 
"2.10.0.1" > "2.1.0.10" returns 1 
"2.0.1" > "1.2000.1" returns 1


'''


def compare_versions(version1: str, version2: str) -> int:
    # Split the versions into parts
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    # Determine the maximum length of both lists
    max_length = max(len(v1_parts), len(v2_parts))
    
    # Pad both lists with zeros to make them the same length
    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))
    
    # Compare each part
    for i in range(max_length):
        if v1_parts[i] > v2_parts[i]:
            return 1
        elif v1_parts[i] < v2_parts[i]:
            return -1
    
    # If all parts are equal, return 0
    return 0


test1 = compare_versions("2", "2.0.0.0.0")  # returns 0
compare_versions("2.1.0", "2.0.1")  # returns 1
compare_versions("2.10.0.1", "2.1.0.10")  # returns 1
compare_versions("2.0.1", "1.2000.1")  # returns 1
compare_versions("2.0.1", "1.2000.1")  # returns 1

print(test1)
