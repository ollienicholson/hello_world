def focus_area_population_narrative(fapop, childrenpop, capacity, occupancy):
    #     '''
    # #  Pass in a dataframe with the following headers
    #     '''
    capacitydelta = capacity - occupancy
    # printfapop = ("{:,}".format(fapop))
    # printchildrenpop = ("{:,}".format(childrenpop))
    # printcapacity = ("{:,}".format(capacity))
    # printoccupancy = ("{:,}".format(occupancy))
    # printcapacitydelta = ("{:,}".format(capacitydelta))
    occupancyrate = round(occupancy/capacity * 100)
    comparisontext = ''
    if capacitydelta >= 0:
        capacitydeltatext = "spaces that are unoccupied"
    else:
        capacitydeltatext = " more children than spaces in the area"

    if occupancyrate > 84:
        comparisontext = "greater than"
    elif occupancyrate == 84:
        comparisontext = "the same as"
    else:
        comparisontext = "less than"

    text_f = f'''\n\nThe total population of the Focus Area is {fapop:,} with {childrenpop:,} children being between the ages of 0 and 4. The total early learning centre capacity is {capacity:,} versus a centre occupancy of {occupancy:,}. This suggests that currently there is {capacitydelta} {capacitydeltatext}. The combined occupancy rate of the centres is {occupancy:,}/{capacity:,} = {occupancyrate}%. This compares to the national average of 84% (187,285/223,522) showing that occupancy is {comparisontext} the national average.\n\n'''
#     # .format(printfapop, printchildrenpop, printcapacity, printoccupancy, printcapacitydelta,
#     #            capacitydeltatext, printoccupancy, printcapacity, occupancyrate, comparisontext)

    print(text_f)
    return text_f


focus_area_population_narrative(32064, 2913, 1844, 1459)

# # ==============================================

# # num1 = 1267, num2 = 1596, calc = (num1 = 1267 / num2 = 1596), num4 = 24 centres, num5 = 95 percent, num6 = 5 centres, num7= 30 percent, num8 = 48 percent


def paragraph_one(num1, num2, num3, num4, num5, num6, num7):
    # calculation on numbers
    # num3 = round(num1 / num2 * 100)

    text_f = f'''This breakdown shows that within the defined Focus Area, Education and Care has an occupancy of {num1:,} out of a possible {num2:,}, representing {round(num1/num2 * 100, 2)}% occupancy across {num3} centres. Kindergarten and Te Kohanga Reo are both occupied at {num4}% across a total of {num5} centres. Playcentre and Homebased Network are occupied at {num6}% and {num7}% respectively.\n\n'''

    print(text_f)
    return text_f


paragraph_one(1267, 1596, 24, 95, 5, 30, 48)

# # ==============================================


def paragraph_two(num1, num2, num3, num4):
    text_f = f'''In the subject Focus Area, we can see that Kindergarten and Homebased are both underweighted relative to national averages - in terms of their presence in the Focus Area. Kindergartens represent {num1}% of the licence places versus {num2}% for the national average. It is interesting to note that even with the lower numbers of Playcentre and Homebased care in the area, the occupancy rates across both care types are low.Education and Care is overweighted relative to the national average, representing {num3}% of the total occupancy and licence positions. In pure numbers this represents {num4} additional licence places and occupancy places above the national average.It is noted that an overweighting or underweighting is purely a measurement against the national average and does not represent an oversupply or undersupply of licence places within the service type.\n\n'''

    print(text_f)
    return text_f


paragraph_two(6, 12, 87, 262)

# # ==============================================


def paragraph_three(num1, num2, num3, num4):

    text_f = f'''This table shows the breakdown of all the Education and Care services in the Focus Area. It provides the occupancy, licence places, the spare capacity (licence places - occupancy), and the occupancy percentage (occupancy/licensed positions). In summary, there are {num1:,} children attending Education and Care services within a total of {num2:,} licence places. This represents spare capacity of {round(num2-num1)} places across this service type within the Focus Area. Of particular note, four centres are responsible for over {num3}% of the spare supply, all with licence sizes above {num4}. This is important to note as it may indicate issues at these specific centres rather than issues that would affect the wider Focus Area.\n\n'''

    print(text_f)
    return text_f

# calc (num3) = num2 - num1
# four centres responsible for <50% spare supply, all with licences over 64 - should this be a calculation?


paragraph_three(1267, 1596, 50, 64)

# # ==============================================


def paragraph_four(num1, num2, num3, num4):

    text_f = f'''Taking the age weighted total of {round(num2*100)}% from this graph, we get a figure of {round(num1*num2):,} ({num1:,} children aged 0 - 4 in Focus Area * {num2} = {round(num1*num2):,}). Of note, this number corresponds directly with the combined licence capacity in the Focus Area being {num3}. This number is also significantly higher than the centre occupancy of {num4:,}. When we consider that {round(num1*num2):,} - {num4:,} is {round((num1*num2)-num4)} - we find that approximately {round((num1*num2)-num4)} children are unaccounted for in this Focus Area. This is a key insight of this report and could be missed unless detailed analysis across all of the datasets is undertaken. Even accounting for margins of error, this still results in a ratio of \033[1m nearly 20% of the 0-4 \033[0m population that would typically be expected to attend ECE - \033[1m not attending ECE \033[0m '''

    print(text_f)
    return text_f
    # first calc = num1*num2 = 1835
    # to get 63% = (num 2 *100)
    # 2nd calc = ((num1*num)-num4) = 376


paragraph_four(2913, 0.63, 1844, 1459)
