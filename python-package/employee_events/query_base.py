# Import any dependencies needed to execute sql queries
from .sql_execution import *

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
Class QueryBase:

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
   def names(self)
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql_query = f''
            select "event_date"
                ,sum("positive_events") as 'Positive Events'
                ,sum("negative_events") as 'Negative Events'
         from "{self.name}"
         left join "employee_events" using ("{self.name}_id")
         where "{self.name}"."{self.name}_id" = {id}
         group by "event_date"
         order by "event_date";
            
        return *.pandas_query(self, sql_query)

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes(self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        sql_query = f''
            select "note_date"
            ,note
            from "notes"
            left join "{self.name}" using ("{self.name}_id")
            where "{self.name}"."{self.name}_id" = {id}
            
        return *.pandas_query(self, sql_query)

