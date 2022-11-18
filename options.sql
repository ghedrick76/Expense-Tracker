DROP TABLE IF EXISTS "Fixed Expenses";
DROP TABLE IF EXISTS "Recurring Expenses";
DROP TABLE IF EXISTS "Non-Recurring Expenses";
DROP TABLE IF EXISTS "Extraneous Expenses";
DROP TABLE IF EXISTS "Income";

CREATE TABLE "Fixed Expenses"(
    "pkExpense" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT DEFAULT "New Expense",
    ""
)