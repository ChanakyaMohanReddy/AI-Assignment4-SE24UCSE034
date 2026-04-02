districts = [
    'Adilabad','Bhadradri Kothagudem','Hanamkonda','Hyderabad','Jagtial',
    'Jangaon','Jayashankar Bhupalpally','Jogulamba Gadwal','Kamareddy',
    'Karimnagar','Khammam','Kumuram Bheem Asifabad','Mahabubabad',
    'Mahabubnagar','Mancherial','Medak','Medchal Malkajgiri','Mulugu',
    'Nagarkurnool','Nalgonda','Narayanpet','Nirmal','Nizamabad',
    'Peddapalli','Rajanna Sircilla','Ranga Reddy','Sangareddy',
    'Siddipet','Suryapet','Vikarabad','Wanaparthy','Warangal',
    'Yadadri Bhuvanagiri'
]

neighbors = {
    'Adilabad':['Nirmal','Kumuram Bheem Asifabad'],
    'Bhadradri Kothagudem':['Mulugu','Mahabubabad','Khammam'],
    'Hanamkonda':['Karimnagar','Siddipet','Jangaon','Warangal','Jayashankar Bhupalpally'],
    'Hyderabad':['Medchal Malkajgiri','Ranga Reddy'],
    'Jagtial':['Nirmal','Nizamabad','Rajanna Sircilla','Karimnagar','Peddapalli','Mancherial'],
    'Jangaon':['Siddipet','Hanamkonda','Warangal','Mahabubabad','Yadadri Bhuvanagiri','Suryapet'],
    'Jayashankar Bhupalpally':['Peddapalli','Mulugu','Warangal','Hanamkonda','Karimnagar'],
    'Jogulamba Gadwal':['Wanaparthy','Nagarkurnool','Narayanpet'],
    'Kamareddy':['Nizamabad','Rajanna Sircilla','Medak','Sangareddy'],
    'Karimnagar':['Jagtial','Peddapalli','Rajanna Sircilla','Siddipet','Hanamkonda','Jayashankar Bhupalpally'],
    'Khammam':['Bhadradri Kothagudem','Mahabubabad','Suryapet'],
    'Kumuram Bheem Asifabad':['Adilabad','Nirmal','Mancherial'],
    'Mahabubabad':['Warangal','Mulugu','Bhadradri Kothagudem','Khammam','Suryapet','Jangaon'],
    'Mahabubnagar':['Vikarabad','Ranga Reddy','Nalgonda','Nagarkurnool','Wanaparthy','Narayanpet'],
    'Mancherial':['Kumuram Bheem Asifabad','Nirmal','Jagtial','Peddapalli'],
    'Medak':['Kamareddy','Sangareddy','Siddipet','Medchal Malkajgiri'],
    'Medchal Malkajgiri':['Sangareddy','Medak','Siddipet','Hyderabad','Ranga Reddy','Yadadri Bhuvanagiri'],
    'Mulugu':['Jayashankar Bhupalpally','Bhadradri Kothagudem','Mahabubabad','Warangal'],
    'Nagarkurnool':['Nalgonda','Mahabubnagar','Wanaparthy','Jogulamba Gadwal'],
    'Nalgonda':['Suryapet','Yadadri Bhuvanagiri','Ranga Reddy','Mahabubnagar','Nagarkurnool'],
    'Narayanpet':['Mahabubnagar','Jogulamba Gadwal'],
    'Nirmal':['Adilabad','Kumuram Bheem Asifabad','Nizamabad','Jagtial','Mancherial'],
    'Nizamabad':['Nirmal','Kamareddy','Jagtial','Rajanna Sircilla'],
    'Peddapalli':['Mancherial','Jagtial','Karimnagar','Jayashankar Bhupalpally'],
    'Rajanna Sircilla':['Nizamabad','Jagtial','Karimnagar','Siddipet','Kamareddy'],
    'Ranga Reddy':['Hyderabad','Medchal Malkajgiri','Vikarabad','Mahabubnagar','Nalgonda','Yadadri Bhuvanagiri'],
    'Sangareddy':['Kamareddy','Medak','Medchal Malkajgiri','Vikarabad'],
    'Siddipet':['Medak','Rajanna Sircilla','Karimnagar','Yadadri Bhuvanagiri','Jangaon','Hanamkonda','Medchal Malkajgiri'],
    'Suryapet':['Jangaon','Mahabubabad','Khammam','Nalgonda','Yadadri Bhuvanagiri'],
    'Vikarabad':['Sangareddy','Ranga Reddy','Mahabubnagar'],
    'Wanaparthy':['Mahabubnagar','Nagarkurnool','Jogulamba Gadwal'],
    'Warangal':['Hanamkonda','Jangaon','Mahabubabad','Mulugu','Jayashankar Bhupalpally'],
    'Yadadri Bhuvanagiri':['Siddipet','Jangaon','Suryapet','Nalgonda','Ranga Reddy','Medchal Malkajgiri']
}

colors = ['Red','Green','Blue','Yellow']

def is_valid(district, color, assignment):
    for n in neighbors[district]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for d in districts:
        if d not in assignment:
            break

    for c in colors:
        if is_valid(d, c, assignment):
            assignment[d] = c
            result = backtrack(assignment)
            if result:
                return result
            del assignment[d]

    return None

solution = backtrack({})

print("Telangana Map Coloring:\n")
for d in solution:
    print(f"{d} -> {solution[d]}")
