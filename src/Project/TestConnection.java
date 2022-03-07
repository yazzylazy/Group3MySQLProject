package Project;

import java.sql.*;

public class TestConnection {
    static final String DB_URL = "";
    static final String USERNAME = "";
    static final String PASSWORD = "";
    static final String QUERY = "";

    public static void main(String[] args){
        try(Connection con = DriverManager.getConnection(DB_URL,USERNAME,PASSWORD);) {

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
