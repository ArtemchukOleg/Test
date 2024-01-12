CREATE TABLE [dbo].[gdf_ergw1000_gwerg__v11_poly](
	[erg_id] [int] NULL,
	[gestein_id] [int] NULL,
	[Shape_STAr] [nvarchar](4000) NULL,
	[Shape_STLe] [nvarchar](4000) NULL,
	[Geom_Col]  geometry
)
GO

select *
from [dbo].[gdf_ergw1000_gwerg__v11_poly]
