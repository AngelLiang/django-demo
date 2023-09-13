# Use the schedule wrapper
from django_q.tasks import schedule

schedule('math.copysign',
         2, -2,
         hook='hooks.print_result',
         schedule_type='D')

# Or create the object directly
from django_q.models import Schedule

Schedule.objects.create(func='math.copysign',
                        hook='hooks.print_result',
                        args='2,-2',
                        schedule_type=Schedule.DAILY
                        )

# In case you want to use q_options
# Specify the broker by using the property broker_name in q_options
schedule('math.sqrt',
         9,
         hook='hooks.print_result',
         q_options={'timeout': 30, 'broker_name': 'broker_1'},
         schedule_type=Schedule.HOURLY)

# Run a schedule every 5 minutes, starting at 6 today
# for 2 hours
# import arrow

# schedule('math.hypot',
#          3, 4,
#          schedule_type=Schedule.MINUTES,
#          minutes=5,
#          repeats=24,
#          next_run=arrow.utcnow().replace(hour=18, minute=0))

# # Use a cron expression
# schedule('math.hypot',
#          3, 4,
#          schedule_type=Schedule.CRON,
#          cron = '0 22 * * 1-5')


# # Restrain a schedule to a specific cluster
# schedule('math.hypot',
#          3, 4,
#          schedule_type=Schedule.DAILY,
#          cluster='my_cluster')
