CREATE DEFINER=`root`@`localhost` PROCEDURE `createUser`(
    IN _name VARCHAR(20),
    IN _email VARCHAR(20),
    IN _password VARCHAR(20)
)
BEGIN
        insert into user
        (
            UiD,
            UserPassword,
            Role
        )
        values
        (
            _name,
            _email,
            _password
        );
END