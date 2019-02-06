hostname MainFirewall
!
interface GigabitEthernet0/0
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/0.248
 vlan 248
 nameif outside
 security-level 0
 ip address 192.168.121.254 255.255.255.248 
!
interface GigabitEthernet0/0.2503
 vlan 2503
 nameif fw-management
 security-level 100
 ip address 172.82.255.1 255.255.255.248 
!
interface GigabitEthernet0/1
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/1.2
 vlan 2
 nameif voicevlan
 security-level 90
 ip address 172.83.1.1 255.255.255.0 
!
interface GigabitEthernet0/1.3
 vlan 3
 nameif xcompany-lan
 security-level 90
 ip address 172.74.101.1 255.255.0.0 
!
interface GigabitEthernet0/1.5
 vlan 5
 nameif sharedresource
 security-level 50
 ip address 172.82.5.1 255.255.255.0 
!
interface GigabitEthernet0/1.30
 vlan 30
 nameif WClients
 security-level 80
 ip address 172.77.101.1 255.255.255.0 
!
interface GigabitEthernet0/1.31
 vlan 31
 nameif WHotSpot
 security-level 40
 ip address 172.77.102.1 255.255.255.0 
!
interface GigabitEthernet0/1.66
 vlan 66
 nameif DIndustries
 security-level 80
 ip address 172.82.66.1 255.255.255.0 
!
interface GigabitEthernet0/1.67
 vlan 67
 nameif PartsIntl
 security-level 80
 ip address 172.82.67.1 255.255.255.0 
!
interface GigabitEthernet0/1.68
 vlan 68
 nameif DFarming
 security-level 80
 ip address 172.82.68.1 255.255.255.0 
!
interface GigabitEthernet0/1.70
 vlan 70
 nameif EFormsInc
 security-level 80
 ip address 172.82.70.1 255.255.255.0 
!
interface GigabitEthernet0/1.71
 vlan 71
 nameif LiveNews
 security-level 80
 ip address 172.82.71.1 255.255.255.0 
!
interface GigabitEthernet0/1.72
 vlan 72
 nameif DeltaGuard
 security-level 80
 ip address 172.82.197.1 255.255.255.0 
!
interface GigabitEthernet0/1.73
 vlan 73
 nameif BioCircle
 security-level 80
 ip address 172.82.73.1 255.255.255.0 
!
interface GigabitEthernet0/1.74
 vlan 74
 nameif RITNS
 security-level 80
 ip address 172.82.74.1 255.255.255.0 
!
interface GigabitEthernet0/1.75
 vlan 75
 nameif SportsAtlantic
 security-level 80
 ip address 172.82.79.1 255.255.255.0 
!
interface GigabitEthernet0/1.76
 vlan 76
 nameif XCompTemp
 security-level 80
 ip address 172.82.76.1 255.255.255.0 
!
interface GigabitEthernet0/1.77
 vlan 77
 nameif IPOCO
 security-level 80
 ip address 172.82.77.1 255.255.255.0 
!
interface GigabitEthernet0/1.80
 vlan 80
 nameif HealthGuide
 security-level 80
 ip address 172.82.80.1 255.255.255.0 
!
interface GigabitEthernet0/1.81
 vlan 81
 nameif PARInc
 security-level 80
 ip address 172.82.81.1 255.255.255.0 
!
interface GigabitEthernet0/1.82
 vlan 82
 nameif ABCTech
 security-level 80
 ip address 172.82.82.1 255.255.255.0 
!
interface GigabitEthernet0/1.83
 vlan 83
 nameif BackBurner
 security-level 80
 ip address 172.82.83.1 255.255.255.0 
!
interface GigabitEthernet0/1.84
 vlan 84
 nameif AdaBiology
 security-level 80
 ip address 172.82.84.1 255.255.255.0 
!
interface GigabitEthernet0/1.85
 vlan 85
 nameif SunEnergy
 security-level 80
 ip address 172.82.85.1 255.255.255.0 
!
interface GigabitEthernet0/1.86
 vlan 86
 nameif TechEnter
 security-level 80
 ip address 172.82.78.1 255.255.255.0 
!
interface GigabitEthernet0/1.90
 vlan 90
 nameif BatteryRUS
 security-level 80
 ip address 172.82.90.1 255.255.255.0 
!
interface GigabitEthernet0/1.92
 vlan 92
 nameif AThermal
 security-level 80
 ip address 172.82.92.1 255.255.255.0 
!
interface GigabitEthernet0/1.93
 vlan 93
 nameif AtlAuto
 security-level 80
 ip address 172.82.91.1 255.255.255.0 
!
interface GigabitEthernet0/1.94
 vlan 94
 nameif AppThermal
 security-level 80
 ip address 172.82.65.1 255.255.255.0 
!
interface GigabitEthernet0/1.95
 vlan 95
 nameif CatStats
 security-level 80
 ip address 172.82.93.1 255.255.255.0 
!
interface GigabitEthernet0/1.96
 vlan 96
 nameif OrgInc
 security-level 80
 ip address 172.82.94.1 255.255.255.0 
!
interface GigabitEthernet0/1.129
 vlan 129
 nameif PernFarming
 security-level 80
 ip address 172.82.129.1 255.255.255.0 
!
interface GigabitEthernet0/1.130
 vlan 130
 nameif IndustrialRec
 security-level 80
 ip address 172.82.130.1 255.255.255.0 
!
interface GigabitEthernet0/1.131
 vlan 131
 nameif XCompScreen
 security-level 80
 ip address 172.82.131.1 255.255.255.0 
!
interface GigabitEthernet0/1.132
 vlan 132
 nameif NickelInc
 security-level 80
 ip address 172.82.132.1 255.255.255.0 
!
interface GigabitEthernet0/1.133
 vlan 133
 nameif GeomMaritime
 security-level 80
 ip address 172.82.133.1 255.255.255.0 
!
interface GigabitEthernet0/1.134
 vlan 134
 nameif Somthingcomplex
 security-level 80
 ip address 172.82.134.1 255.255.255.0 
!
interface GigabitEthernet0/1.135
 vlan 135
 nameif NewMagz
 security-level 80
 ip address 172.82.135.1 255.255.255.0 
!
interface GigabitEthernet0/1.138
 vlan 138
 nameif SomethingTech
 security-level 80
 ip address 172.82.87.1 255.255.255.0 
!
interface GigabitEthernet0/1.140
 vlan 140
 nameif IntegratedElec
 security-level 80
 ip address 172.82.75.1 255.255.255.0 
!
interface GigabitEthernet0/1.141
 vlan 141
 nameif CleanPower
 security-level 80
 ip address 172.82.141.1 255.255.255.0 
!
interface GigabitEthernet0/1.144
 vlan 144
 nameif Damswells
 security-level 80
 ip address 172.82.136.1 255.255.255.0 
!
interface GigabitEthernet0/1.145
 vlan 145
 nameif GeneralMeds
 security-level 80
 ip address 172.82.89.1 255.255.255.0 
!
interface GigabitEthernet0/1.146
 vlan 146
 nameif DentalRecords
 security-level 80
 ip address 172.82.193.1 255.255.255.0 
!
interface GigabitEthernet0/1.192
 vlan 192
 nameif SomeProducts
 security-level 80
 ip address 172.82.192.1 255.255.255.0 
!
interface GigabitEthernet0/1.199
 vlan 199
 nameif NovaEngines
 security-level 80
 ip address 172.82.194.1 255.255.255.0 
!
interface GigabitEthernet0/1.249
 vlan 249
 nameif transit
 security-level 100
 ip address 172.85.255.10 255.255.255.0 
!
interface GigabitEthernet0/1.255
 vlan 255
 nameif management2
 security-level 100
 ip address 172.10.10.1 255.255.255.0 
!
interface GigabitEthernet0/2
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/3
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/4
 shutdown
 no nameif
 no security-level
 no ip address
!
interface GigabitEthernet0/5
 shutdown
 no nameif
 no security-level
 no ip address
!
interface Management0/0
 management-only
 nameif management
 security-level 100
 ip address 192.168.1.1 255.255.255.0 
!
access-list transit_access_in extended permit object-group SERVICES-INSIDE-XCOMP-RADIUS object MGMT-TRANSIT object SERVER-INSIDE-XCOMP-RADIUS 
access-list transit_access_in extended permit ip object MGMT-INTERNAL object MGMT-AAA 
access-list transit_access_in extended permit ip object VPN-XCOMPANY object LAN-XCOMPANY 
access-list transit_access_in extended permit ip object VPN-XCOMPANY object LAN-VOIP 
access-list transit_access_in extended permit ip object VPN-AdaBiology object LAN-AdaBiology 
access-list transit_access_in extended permit ip object VPN-BioCircle object LAN-BioCircle 
access-list transit_access_in extended permit ip object VPN-DIndustries object LAN-DIndustries 
access-list transit_access_in extended permit ip object VPN-XCOMPTEMP object LAN-XCOMPTEMP 
access-list transit_access_in extended permit ip object VPN-RITNS object LAN-RITNS 
access-list transit_access_in extended permit ip object VPN-PartsIntl object LAN-PartsIntl 
access-list transit_access_in extended permit ip object VPN-IntegratedElec object LAN-IntegratedElec 
access-list transit_access_in extended permit ip object VPN-IndustrialRec object LAN-IndustrialRec 
access-list transit_access_in extended permit ip object VPN-GeomMaritime object LAN-GeomMaritime 
access-list transit_access_in extended permit ip object VPN-Damswells object LAN-Damswells 
access-list transit_access_in extended permit ip object VPN-CleanPower object LAN-CleanPower 
access-list global_access extended permit object-group SERIVCES-OUTSIDE-XCOMP-EMAIL any object SERVER-INSIDE-XCOMP-2 
access-list global_access extended permit object-group SERVICES-OUTSIDE-XCOMP-DNS any object SERVER-INSIDE-XCOMP-3 
access-list global_access extended permit object-group SERVICES-OUTSIDE-XCOMP-4 any object SERVER-INSIDE-XCOMP-4 
access-list global_access extended permit object-group SERVICES-OUTSIDE-XCOMP-6 any object SERVER-INSIDE-XCOMP-6 
access-list global_access extended permit tcp object-group DM_INLINE_NETWORK_1 object SERVER-INSIDE-XCOMP-24 eq 48620 
access-list global_access extended permit object-group SERVICES-OUTSIDE-XCOMP-27 any object SERVER-INSIDE-XCOMP-27 
access-list global_access extended permit ip any object SERVER-INSIDE-VOIP-78 
access-list global_access extended permit ip any object SERVER-INSIDE-DeltaGuard-88 
access-list global_access extended permit ip any object SERVER-INSIDE-DeltaGuard-89 
access-list global_access extended permit ip any object SERVER-INSIDE-FORERUN-77 
access-list global_access extended permit ip any object SERVER-INSIDE-PERNIX-64 
access-list global_access extended permit ip any object SERVER-INSIDE-CLINICAL-69 
access-list global_access extended permit ip any object SERVER-INSIDE-CLINICAL-72 
access-list global_access extended permit ip any object SERVER-INSIDE-XCOMPSCREEN-65 
access-list global_access extended permit ip any object SERVER-INSIDE-NickelInc-66 
access-list global_access extended permit ip any object SERVER-INSIDE-NickelInc-70 
access-list global_access extended permit ip any object SERVER-INSIDE-NickelInc-71 
access-list global_access extended permit ip any object SERVER-INSIDE-GENOME-67 
access-list global_access extended permit ip any object SERVER-INSIDE-NewMagz-68 
access-list global_access extended permit ip any object SERVER-INSIDE-NewMagz-76 
access-list global_access extended permit ip any object SERVER-INSIDE-Damswells-85 
access-list global_access extended permit ip any object SERVER-INSIDE-Damswells-86 
access-list global_access extended permit ip any object SERVER-INSIDE-Damswells-87 
access-list global_access extended permit ip any object SERVER-INSIDE-SMTPSVCS-224 
access-list global_access extended permit ip any object SERVER-INSIDE-DENSITAS-79 
access-list global_access extended permit ip any object SERVER-INSIDE-DENSITAS-80 
access-list global_access extended permit ip any object SERVER-INSIDE-DENSITAS-81 
access-list global_access extended permit ip any object SERVER-INSIDE-NOVONIX-82 
access-list global_access extended permit ip any object SERVER-INSIDE-NOVONIX-83 
access-list global_access extended permit ip any object SERVER-INSIDE-NOVONIX-84 
access-list global_access extended permit ip object INSIDE-EVERYTHING object LAN-SHAREDRESOURCES 
access-list global_access extended permit ip object OUTSIDE-XCOMPANY-ALL object LAN-SHAREDRESOURCES 
access-list global_access extended deny ip object INSIDE-EVERYTHING object INSIDE-EVERYTHING 
access-list global_access extended permit ip object INSIDE-EVERYTHING any 
access-list xcompany-lan_access_in extended permit ip object LAN-XCOMPANY object LAN-VOIP 
access-list xcompany-lan_access_in extended permit ip object LAN-XCOMPANY object MGMT-INTERNAL 
access-list xcompany-lan_access_in extended permit ip object LAN-XCOMPANY object LAN-SomeProducts 
access-list management2_access_in extended permit object-group SERVICES-INSIDE-XCOMP-RADIUS object MGMT-INTERNAL object SERVER-INSIDE-XCOMP-RADIUS 
access-list management2_access_in extended permit ip object MGMT-INTERNAL object SERVER-INSIDE-XCOMP-UNIFI 
access-list management2_access_in extended permit ip object MGMT-INTERNAL object SERVER-INSIDE-XCOMP-UNIFI-NEW 
access-list management2_access_in extended permit ip object MGMT-INTERNAL object MGMT-AAA 
access-list sharedresource_access_in extended permit ip object LAN-SHAREDRESOURCES object SERVER-INSIDE-SHARED-SMTP 
access-list SomeProducts_access_in extended permit ip object LAN-SomeProducts object LAN-XCOMPANY 
access-list fw-management_access_in extended permit ip object MGMT-AAA object MGMT-INTERNAL 
access-list fw-management_access_in extended permit ip object MGMT-AAA-OLD object MGMT-INTERNAL 
access-list WirelessHotspot_access_in extended permit ip object LAN-WIRELESSHOTSPOT object SERVER-INSIDE-XCOMP-UNIFI 
access-list WirelessHotspot_access_in extended permit ip object LAN-WIRELESSHOTSPOT object SERVER-INSIDE-XCOMP-UNIFI-NEW 
access-list WirelessHotspot_access_in extended deny ip object LAN-WIRELESSHOTSPOT object LAN-SHAREDRESOURCES inactive 
access-list voicevlan_access_in extended permit ip object LAN-VOIP object LAN-XCOMPANY 
access-list WirelessClients_access_in extended permit ip object LAN-WIRELESSCLIENTS object LAN-VOIP 
!
: end
