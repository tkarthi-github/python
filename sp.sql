CREATE PROCEDURE usp_UpdateExelaTaxDetails
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE IM
    SET IM.TaxCode = HM.TaxCode
    FROM EXELA_Item_Master IM
    INNER JOIN (
        SELECT HSNCode, TaxCode
        FROM HSNMaster HM1
        WHERE HSNCode IN (
            SELECT HSNCode
            FROM HSNMaster
            GROUP BY HSNCode
            HAVING COUNT(*) = 1
        )
    ) HM ON IM.HSNCode = HM.HSNCode
    WHERE IM.TaxCode IS NULL OR LEN(RTRIM(IM.TaxCode)) = 0;

    
    UPDATE IM
    SET 
        IM.SGST = DD.SGST,
        IM.CGST = DD.CGST,
        IM.ISGT = DD.ISGT,
        IM.UTGST = DD.UTGST,
        IM.Rate = DD.Rate
    FROM EXELA_Item_Master IM
    INNER JOIN SSL_DropDownFields DD ON IM.TaxCode = DD.FieldoutputValue
    WHERE 
        (IM.SGST IS NULL OR LEN(RTRIM(IM.SGST)) = 0) AND
        (IM.CGST IS NULL OR LEN(RTRIM(IM.CGST)) = 0) AND
        (IM.ISGT IS NULL OR LEN(RTRIM(IM.ISGT)) = 0) AND
        (IM.UTGST IS NULL OR LEN(RTRIM(IM.UTGST)) = 0) AND
        (IM.Rate IS NULL OR LEN(RTRIM(IM.Rate)) = 0);
END;
GO