package Project;

import java.sql.*;

public class TestConnection {
    static final String DB_URL = "jdbc:mysql://us-cdbr-east-05.cleardb.net:3306/heroku_a9a58dad9c5e526";
    static final String USERNAME = "b559517d77ae6e";
    static final String PASSWORD = "74499144";
    static final String QUERY = "SELECT * FROM persons";

    public static void main(String[] args){
        try(Connection con = DriverManager.getConnection(DB_URL,USERNAME,PASSWORD);) {
            Statement st = con.createStatement();
            ResultSet rt = st.executeQuery(QUERY);
            System.out.println("ID\t\tLAST NAME\t\tFIRST NAME\t\tADDRESS\t\tCITY");
            while(rt.next()){
                System.out.println(rt.getString("PersonID"));
                System.out.println("\t\t"+rt.getString("LastName"));
                System.out.println("\t\t"+rt.getString("FirstName"));
                System.out.println("\t\t"+rt.getString("Address"));
                System.out.println("\t\t"+rt.getString("City"));
            }
            rt.close();
            st.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


    /*

     Statement st = con.createStatement();
            ResultSet rt = st.executeQuery(QUERY);
            System.out.println("Aname\t\tBirthday");
            while(rt.next()){
                System.out.println(rt.getString("aname"));
                System.out.println("\t\t"+rt.getString("date of birth"));
            }
            rt.close();
            st.close();
     */
}
