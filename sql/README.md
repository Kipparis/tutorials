# Basic syntax

If you want to refer to column, you can do it explicitly by using double-quotes.
For example, if you have column `group` (same as function in sql), you want to
use "group" in SQL statement.  

# Query clause order (order in which operations are work)

1. `SELECT`  
2. `FROM`  
3. `WHERE`  
4. `GROUP BY`  
5. `HAVING`  
6. `ORDER BY`  

## select

Changes how output is showed. Can use aggregation, CASE statement.  

## where

Filters output. Works before aggregation.  

## count

+ `count(*)`: counts all rows  
+ `count(column)`: counts all rows where "column" is not null  
+ `count(1)`: counts first column passed in `SELECT` clause  

When using `count` with `case`, `case` produces like new column (instead of just
single value as I've thought before). So in structure like  

```sql
COUNT(CASE WHEN year = 'FR' THEN 1 ELSE NULL END) as fr_count
```

It will:  

1.  Produce new column for each row where 1 if year field in row has value of
    'FR' and null in other cases.  
2.  Calculate number of non-null rows.  

## group by

`count`, `avg` and `sum` aggregate across the entire table by default. If you
want to aggregate only part of it, you want to use `group by`. So, if you want
to aggregate values by each year, you use `GROUP BY year`.  

You can use columns' aliases  

# Control flow

## case

Always goes in the `SELECT` clause.  

`case` statement represents if/else logic. Syntax is `CASE WHEN ... THEN ...
[WHEN ... THEN ...] [ELSE ...] END`. `ELSE` part capures values unhandled by
`when` clauses.  

`case` actually produces new column. So, when it used inside of aggregate
function, later will aggregate across column, produced by `case`  
