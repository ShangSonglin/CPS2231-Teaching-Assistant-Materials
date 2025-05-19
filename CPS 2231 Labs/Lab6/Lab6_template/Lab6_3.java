public class Lab6_3 {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java Lab6_3 <command> [amount]");
            return;
        }

        String command = args[0];
        switch (command) {
            case "create":
                testConstructor();
                break;
            case "getset":
                testGetterSetter();
                break;
            case "deposit":
                if (args.length < 2) {
                    System.out.println("Usage: java Lab6_3 deposit <amount>");
                    return;
                }
                testDeposit(Double.parseDouble(args[1]));
                break;
            case "withdraw":
                if (args.length < 2) {
                    System.out.println("Usage: java Lab6_3 withdraw <amount>");
                    return;
                }
                testWithdraw(Double.parseDouble(args[1]));
                break;
        }
    }

    // Test methods are provided to ensure correct output format
    private static void testConstructor() {
        Account account = new Account("A1001", "John Doe", 1000.00);
        System.out.println("Testing constructor...");
        System.out.println("Created account: " + account);
        System.out.println("Fields initialized correctly: OK");
        System.out.println("Created account with custom values: OK");
        System.out.println("All constructor tests passed!");
    }

    private static void testGetterSetter() {
        Account account = new Account("A1001", "John Doe", 1000.00);
        System.out.println("Testing getter/setter methods...");
        System.out.println("Initial values:");
        System.out.println(account);
        
        System.out.println("\nSetting new values...");
        account.setAccountNumber("B2002");
        account.setAccountHolder("Jane Smith");
        account.setBalance(2500.00);
        
        System.out.println("New account number: " + account.getAccountNumber());
        System.out.println("New account holder: " + account.getAccountHolder());
        System.out.println("New balance: " + formatCurrency(account.getBalance()));
        
        System.out.println("\nGetting values after update:");
        System.out.println(account);
        System.out.println("All getter/setter tests passed!");
    }

    private static void testDeposit(double amount) {
        Account account = new Account("A1001", "John Doe", 1000.00);
        System.out.println("Testing deposit...");
        System.out.println("Initial balance: " + formatCurrency(account.getBalance()));
        System.out.println("Depositing: " + formatCurrency(amount));
        account.deposit(amount);
        System.out.println("New balance: " + formatCurrency(account.getBalance()));
        System.out.println("Deposit test passed!");
    }

    private static void testWithdraw(double amount) {
        Account account = new Account("A1001", "John Doe", 1000.00);
        
        if (amount > account.getBalance()) {
            System.out.println("Testing insufficient funds...");
            System.out.println("Initial balance: " + formatCurrency(account.getBalance()));
            System.out.println("Attempting to withdraw: " + formatCurrency(amount));
            account.withdraw(amount);
            System.out.println("Insufficient funds");
            System.out.println("Balance unchanged: " + formatCurrency(account.getBalance()));
            System.out.println("Insufficient funds test passed!");
        } else {
            System.out.println("Testing withdrawal...");
            System.out.println("Initial balance: " + formatCurrency(account.getBalance()));
            System.out.println("Withdrawing: " + formatCurrency(amount));
            account.withdraw(amount);
            System.out.println("New balance: " + formatCurrency(account.getBalance()));
            System.out.println("Withdrawal test passed!");
        }
    }

    private static String formatCurrency(double amount) {
        return String.format("$%,.2f", amount);
    }
}

// TODO: Create the Account class here
// The class should have:
// 1. Private fields for accountNumber, accountHolder, and balance
// 2. A constructor that initializes all fields
// 3. Getter and setter methods for all fields
// 4. deposit() method that increases the balance
// 5. withdraw() method that decreases the balance
// 6. toString() method that returns the account details in the format:
//    "Account #<number>, Holder: <name>, Balance: $<amount>"
class Account {
    // Your code here
} 