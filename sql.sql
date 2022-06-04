select Branch_ID, Branch_Name from Branch 
where (select Region from Area where Region = "Selangor");

select Region, AVG(Population)  from Area group by AVG(Population) DESC;