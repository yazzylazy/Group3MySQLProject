package Project;

import java.sql.*;

public class TestConnection {
    static final String DB_URL = "jdbc:mysql://us-cdbr-east-05.cleardb.net:3306/heroku_a9a58dad9c5e526";
    static final String USERNAME = "b559517d77ae6e";
    static final String PASSWORD = "74499144";
    static final String QUERY = "SELECT * FROM user";

    public static void main(String[] args){
        try(Connection con = DriverManager.getConnection(DB_URL,USERNAME,PASSWORD);) {
            Statement st = con.createStatement();
            ResultSet rt = st.executeQuery(QUERY);
            System.out.println("UiD\t\tUserPassword\t\tRole");
            while(rt.next()){
                System.out.println(rt.getString("UiD"));
                System.out.print("\t\t"+rt.getString("UserPassword"));
                System.out.print("\t\t"+rt.getString("Role"));
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
