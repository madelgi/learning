# Character Strings and Formatted I/O

1. TODO

2. Assuming that each of the following examples is part of a complete program, what
   will each one print?

   a. `printf("He sold the painting for $%2.2f.\n", 2.345e2);`

       Should return "He sold the painting for 234.50".

   b. `printf("%c%c%c\m", 'H', 105, '\41');`

       "Hi!"

3. TODO

4. Find the error in the following code:

   ```C
   define B booboo
   define X 10
   main(int)
   {
       int age;
       char name;
       printf("Please enter your first name.");
       scanf("%s", name);
       printf("All right, %c, what's your age?\n", name);
       scanf("%f", age);
       xp = age + X
       printf("That's a %s! You must be at least %d.\n", B, xp);
       rerun 0;
   }
   ```

   **Answer**: Here is the corrected code:

   ```C
   #define B "booboo"
   #define X 10
   int main()
   {
       int age;
       char[40] name;
       printf("Please enter your first name.\n");
       scanf("%s", name);
       printf("All right, %s, what's your age?\n", name);
       scanf("%d", age);
       int xp = age + X
       printf("That's a %s! You must be at least %d.\n", B, xp);
       return 0;
   }
   ```

5. Suppose a program starts as follows:

   ```C
   #define BOOK "War and Peace"
   int main(void)
   {
       float cost = 12.99;
       float percent = 80.0;
   ```

   Construct a `printf()` statement that uses `BOOK`, `cost`, and `percent` to print
   the following:

   ```
   This copy of "War and Peace" sells for $12.99.
   That is 80% of list.
   ```

   **Answer:**

   ```C
   printf("This copy of %s sells for %.2f.\n", BOOK, cost);
   printf("That is %d%% of list.\n", percent);
   ```
