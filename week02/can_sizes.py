import math

best_storage_eff = 0
best_storage_name = ""
best_cost_eff = 0
best_cost_name = ""

def main():
   compute_storage_efficiency("#1 Picnic", 8.73, 11.59, 0.28)
   compute_storage_efficiency("#1 Tall", 8.73, 11.59, 0.43)
   compute_storage_efficiency("#2", 8.73, 11.59, 0.45)
   compute_storage_efficiency("#2.5", 10.32, 11.91, 0.61)
   compute_storage_efficiency("#3 Cylinder", 10.79, 17.78, 0.86)
   compute_storage_efficiency("#5", 13.02, 14.29, 0.83)
   compute_storage_efficiency("#6Z", 5.40, 8.89, 0.22)
   compute_storage_efficiency("#8Z short", 6.83, 7.62, 0.26)
   compute_storage_efficiency("#10", 15.72, 17.78, 1.53)
   compute_storage_efficiency("#211", 6.83, 12.38, 0.34)
   compute_storage_efficiency("300", 7.62, 11.27, 0.38)
   compute_storage_efficiency("#303", 8.10, 11.11, 0.42)


def compute_storage_efficiency(name, radius, height, cost):
     global best_storage_eff, best_storage_name, best_cost_eff, best_cost_name
     
     area = compute_surface_area(radius, height)
     volume = compute_volume(radius, height)
     cost_eff = compute_cost_efficiency(radius, height, cost)
     efficiency = volume / area

     print(f"{name} | Volume = {volume:.2f} | Area = {area:.2f} | Efficiency = {efficiency:.2f} | Cost = ${cost_eff:.2f}")
    
    #update best storage efficiency

     if efficiency > best_storage_eff:
          best_storage_eff = efficiency
          best_storage_name = name

     if cost_eff > best_cost_eff:
          best_cost_eff = cost_eff
          best_cost_name = name

def compute_surface_area(radius, height):
      surfaceArea = 2 * math.pi * radius * (radius + height)
      return surfaceArea

def compute_volume(radius, height):
        vol = math.pi * radius ** 2 * height
        return vol

def compute_cost_efficiency(radius, height, cost):
     volume = compute_volume(radius, height)
     return volume/cost
     
main()

# final result 

print("\n=== Best Result ===")
print(f"Best Storage Efficiency: {best_storage_name} ({best_storage_eff:.2f})")
print(f"Best Cost Efficiency: {best_cost_name} ({best_cost_eff:.2f})")






















# def main():
#     compute_storage_efficiency("#1 Picnic", 6.83, 10.16, 0.28)
#     compute_storage_efficiency("#1 Tall", 7.78, 11.91, 0.43)
#     compute_storage_efficiency("#2", 8.73, 11.59, 0.45)
#     compute_storage_efficiency("#2.5", 10.32, 11.91, 0.61)
#     compute_storage_efficiency("#3 Cylinder", 10.79, 17.78, 0.86)
#     compute_storage_efficiency("#5", 13.02, 14.29, 0.83)
#     compute_storage_efficiency("#6Z", 5.40, 8.89, 0.22)
#     compute_storage_efficiency("#8Z short", 6.83, 7.62, 0.26)
#     compute_storage_efficiency("#10", 15.72, 17.78, 1.53)
#     compute_storage_efficiency("#211", 6.83, 12.38, 0.34)
#     compute_storage_efficiency("300", 7.62, 11.27, 0.38)
#     compute_storage_efficiency("#303", 8.10, 11.11, 0.42)

#     # final result after all calls
#     print("\n=== Best Results ===")
#     print(f"Best Storage Efficiency: {best_storage_name} ({best_storage_eff:.2f})")
#     print(f"Best Cost Efficiency: {best_cost_name} ({best_cost_eff:.2f})")


# def compute_storage_efficiency(name, radius, height, cost):
#     global best_storage_eff, best_storage_name, best_cost_eff, best_cost_name

#     area = compute_surface_area(radius, height)
#     volume = compute_volume(radius, height)
#     cost_eff = compute_cost_efficiency(radius, height, cost)
#     efficiency = volume / area

#     print(f"{name} | Volume = {volume:.2f} | Area = {area:.2f} | "
#           f"Efficiency = {efficiency:.2f} | Cost Efficiency = {cost_eff:.2f}")

#     # update best storage efficiency
#     if efficiency > best_storage_eff:
#         best_storage_eff = efficiency
#         best_storage_name = name

#     # update best cost efficiency
#     if cost_eff > best_cost_eff:
#         best_cost_eff = cost_eff
#         best_cost_name = name


# def compute_surface_area(radius, height):
#     return 2 * math.pi * radius * (radius + height)

# def compute_volume(radius, height):
#     return math.pi * radius ** 2 * height

# def compute_cost_efficiency(radius, height, cost):
#     volume = compute_volume(radius, height)
#     return volume / cost


# main()
