
# from django.db.models import Avg
# from my_new_app.models import Record
# from django.http import JsonResponse
# from django.shortcuts import render
# from my_new_app.models import Record
# from django.db import connection




# def total_records(request):
#     with connection.cursor() as cursor:
#         cursor.execute(f"SELECT COUNT(*) FROM my_new_app_mymodel")
#         result = cursor.fetchone()

#     total_records = result[0] if result is not None else 0
#     return render(request, 'total_records.html', {'total_records': total_records})


# def calculate_mean( ):
#     mean_value = Record.objects.all().aggregate(mean_value=Avg('value_field'))['mean_value']
#     return JsonResponse({'mean': mean_value})


# def calculate_median(request):
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY value_field) FROM my_new_app_mymodel"
#         )
#         result = cursor.fetchone()

#     median_value = result[0] if result is not None else None
#     return render(request, 'median.html', {'median_value': median_value})


# # from django.db.models.expressions import PercentRank
# # from django.contrib.postgres.fields import PercentRangeField
# # from django.http import JsonResponse

# # def calculate_percentile_25(request):
# #     # Calculate 25th percentile value
# #     percentile_25_value = (
# #         MyModel.objects.all()
# #         .aggregate(percentile_25=Percentile('value_field', 25))['percentile_25']
# #     )
# #     return JsonResponse({'25th_percentile': percentile_25_value})

# from my_new_app.models import Record

# def calculate_percentile(queryset, percentile):
#     count = queryset.count()
#     index = int(count * percentile / 100)
#     if count % 2 == 0:
#         # If the count is even
#         return (queryset[index-1].salary + queryset[index].salary) / 2
#     else:
#         return queryset[index].salary

# def calculate_25th_percentile(request):
#     # Assuming 'salary' is the field representing the salary in the MyModel
#     queryset = Record.objects.order_by('salary')
#     percentile_25 = calculate_percentile(queryset, 25)
#     return JsonResponse({'25th_percentile_salary': percentile_25})

# def calculate_75th_percentile(request):
#     # Assuming 'salary' is the field representing the salary in the MyModel
#     queryset = Record.objects.order_by('salary')
#     percentile_75 = calculate_percentile(queryset, 75)
#     return JsonResponse({'75th_percentile_salary': percentile_75})

# from django.db.models import Avg
# from my_new_app.models import Record
# from django.http import JsonResponse
# from django.shortcuts import render
# index =0
# ...

# def calculate_percentile(queryset, percentile):
#     count = queryset.count()
#     index = int(count * percentile / 100)
#     if count % 2 == 0:
#         # If the count is even
#         return (queryset[index-1].value_field + queryset[index].value_field) / 2
#     else:
#         return queryset[index].value_field

# def calculate_25th_percentile(request):
#     # Assuming 'value_field' is the field representing the value in the Record model
#     queryset = Record.objects.order_by('value_field')
#     percentile_25 = calculate_percentile(queryset, 25)
#     return JsonResponse({'25th_percentile_value': percentile_25})

# def calculate_75th_percentile(request):
#     # Assuming 'value_field' is the field representing the value in the Record model
#     queryset = Record.objects.order_by('value_field')
#     percentile_75 = calculate_percentile(queryset, 75)
#     return JsonResponse({'75th_percentile_value': percentile_75})

# from my_new_app.models import Record
# from django.http import JsonResponse

# def calculate_percentiles(request):
#     salaries = list(Record.objects.values_list('WAGE_RATE_OF_PAY_FROM', flat=True).order_by('WAGE_RATE_OF_PAY_FROM'))

#     if not salaries:
#         return JsonResponse({'error': 'No data available'})

#     count = len(salaries)
#     index_25th = int(0.25 * count)
#     index_75th = int(0.75 * count)

#     sorted_salaries = sorted(salaries)

#     salary_25th = sorted_salaries[index_25th] if index_25th < count else sorted_salaries[-1]
#     salary_75th = sorted_salaries[index_75th] if index_75th < count else sorted_salaries[-1]

#     return JsonResponse({
#         '25th_percentile_salary': salary_25th,
#         '75th_percentile_salary': salary_75th
#     })

# I. Number of results: Count the total number of records in the database.
# def Number_of_results(input_list):
#     num_elements = len(input_list)
#     return num_elements

# #II. Mean salary: Calculate the mean (average) salary of H1B applicants.
# def mean_salary(input_list):
#     if len(input_list) == 0:
#         return None

#     total = sum(input_list)
#     mean = total / len(input_list)
#     return mean

# #III. Median salary: Calculate the median salary of H1B applicants.
# def median_salary(input_list):
#     sorted_list = sorted(input_list)
#     n = len(sorted_list)

#     if n % 2 == 0:
#         middle1 = sorted_list[n // 2 - 1]
#         middle2 = sorted_list[n // 2]
#         median = (middle1 + middle2) / 2
#     else:
#         median = sorted_list[n // 2]
#     return median

# #IV. 25% percentile salary: Calculate the 25th percentile salary.
# def salary_25(input_list):
#     sorted_list = sorted(input_list)
#     n = len(sorted_list)
#     h = int(0.25 * (n - 1))

#     if n % 4 == 0:
#         value1 = sorted_list[h]
#         value2 = sorted_list[h + 1]
#         percentile_25 = (value1 + value2) / 2
#     else:
#         percentile_25 = sorted_list[h]

#     return percentile_25

# #V. 75% percentile salary: Calculate the 75th percentile salary.
# def salary_75(input_list):
#     sorted_list = sorted(input_list)
#     n = len(sorted_list)
#     h = int(0.75 * (n - 1))

#     if n % 4 == 0:
#         value1 = sorted_list[h]
#         value2 = sorted_list[h + 1]
#         percentile_75 = (value1 + value2) / 2
#     else:
#         percentile_75 = sorted_list[h]

#     return percentile_75

from django.db.models import Avg
from my_new_app.models import Record
from django.http import JsonResponse
from statistics import median

def calculate_statistics(request):
    # I. Count the total number of records in the database.
    total_records = Record.objects.count()

    # II. Calculate the mean (average) salary of H1B applicants.
    mean_salary = Record.objects.aggregate(mean_salary=Avg('salary'))['mean_salary']

    # III. Calculate the median salary of H1B applicants.
    salaries = list(Record.objects.values_list('salary', flat=True))
    median_salary = median(salaries)

    # IV. Calculate the 25th percentile salary.
    sorted_salaries = sorted(salaries)
    index_25th = int(0.25 * len(sorted_salaries))
    percentile_25 = sorted_salaries[index_25th]

    # V. Calculate the 75th percentile salary.
    index_75th = int(0.75 * len(sorted_salaries))
    percentile_75 = sorted_salaries[index_75th]

    return JsonResponse({
        'total_records': total_records,
        'mean_salary': mean_salary,
        'median_salary': median_salary,
        '25th_percentile_salary': percentile_25,
        '75th_percentile_salary': percentile_75
    })