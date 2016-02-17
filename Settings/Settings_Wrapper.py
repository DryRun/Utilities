"""
DB Wrapper Settings. To make things dynamic,
you can set the quantities you want to query for from this config.
Importing is static - no dynamic module importing of settings
"""

runinfo_db_name = "cms_hcl_runinfo/run2009info"

quantitymap = {
	"NEVENTS" : ("STRING_VALUE","CMS.HCAL%:TRIGGERS"),
	"CONFIG_OLD" : ("STRING_VALUE", "CMS.HCAL%:FM_FULLPATH"),
	"CONFIG_NEW" : ("STRING_VALUE", "CMS.HCAL%:LOCAL_RUN_KEY"),
	"TIME" : ("TIME", "CMS.HCAL%")
}
