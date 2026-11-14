# Logic Run 1 - The Underground Museum
# 12 | November | 2026
# Objective : Build a program that analyses the daily activity of an underground museum

exhibitions = {
    134 : "Potions and Poisons",
    98 : "Magical Wands",
    167 : "Purple Frogs",
    107 : "Enchanted Books",
    93 : "Phoenix Feathers"
}
print("====== VISITOR COUNT ======")
for exhibition in exhibitions :
    print(f"{exhibition} -> {exhibitions[exhibition]}")
print("===========================")

print(f"Total number of visitors : {sum(exhibitions.keys())}") # just learned this + a few other dict methods like 0.34 seconds ago

for people in exhibitions.keys() :
        print(f"EXHIBIT - {exhibitions[people]}")
        if people > 100 :
            print("[CAUTION] : Room overloaded. Professor Goblin is emotionally damaged.")
        else :
            print("The room is safe from nuclear explosions. For now.")

most_popular_exhibit = max(exhibitions.keys())
least_crowded_exhibit = min(exhibitions.keys())

print("-x-x-x-x-x-x-x-x-x-x-x- FINAL REPORT -x-x-x-x-x-x-x-x-x-x-x-")
print(f"Available exhibitions : {exhibitions.values()}")
print(f"Recorded visitors per exhibit : {exhibitions.keys()}")
print(f"Total number of visitors : {sum(exhibitions.keys())}") 
print(f"Most popular exhibit : {exhibitions[most_popular_exhibit]}")
print(f"Least crowded exhibit : {exhibitions[least_crowded_exhibit]}")

# presentation needs improvement : make the final report display the exhibit names n counts in clean, 
# readable format rather than displaying direct dict format