/*

This file is a modified version of direct-grid.js found in the Ext JS 4 package.

Copyright (c) 2011 Sencha Inc

Contact:  http://www.sencha.com/contact

GNU General Public License Usage
This file may be used under the terms of the GNU General Public License version 3.0 as published by the Free Software Foundation and appearing in the file LICENSE included in the packaging of this file.  Please review the following information to ensure the GNU General Public License version 3.0 requirements will be met: http://www.gnu.org/copyleft/gpl.html.

If you are unsure which license is appropriate for your use, please contact the sales department at http://www.sencha.com/contact.

*/
var proxy;

Ext.onReady(function() {
//	Ext.direct.Manager.addProvider(Ext.app.REMOTING_API);
/*
	var p = Ext.direct.Manager.addProvider(Ext.app.REMOTING_API);
	console.log(p);
	//console.log(QueryDatabase.getResults);
	QueryDatabase.getResults = function () { console.log(arguments); };
*/

/*
	var ZendFrameworkProvider = Ext.extend(Ext.direct.RemotingProvider, {
	});

	Ext.Direct.PROVIDERS['zfprovider'] = ZendFrameworkProvider;

	Ext.direct.Manager.addProvider({
		'type': 'zfprovider'
	});

	Ext.Direct.addProvider(Ext.apply(Ext.app.REMOTING_API, {
      'type': 'zfprovider',
      'url': Ext.app.JSONRPC_API.target
	}));
*/



	//added model inside onready
/*
	Ext.define('PersonalInfo', {
		extend: 'Ext.data.Model',
		fields: ['ID', 'NAME', 'ADDRESS', 'STATE']
	});
*/

	var PersonalInfo = Ext.regModel('PersonalInfo', {
		fields: ['ID', 'NAME', 'ADDRESS', 'STATE'],
		proxy: {
			data: data,
			type: 'cachedrest',
			api: {
            create: undefined,
            read: 'http://example.com/api#getTables',
            update: undefined,
            destroy: undefined
         },
			reader: {
				type: 'json',
				root: 'rows'
			}
		}
	});
/*
	var personalInfo = new PersonalInfo({'ID': 5,
													 'NAME': 'Ed Spencer',
													 'ADDRESS': 'ST.Stree 13',
													 'STATE': 'BY'});
	personalInfo.save();
*/
/*
	proxy = Ext.create('MyApp.data.CachedRestProxy',
								  {
			data: data,
			type: 'cachedrest',
			reader: {
				type: 'json',
				root: 'rows'
			}
		});
*/

	//separated store into unique var for guaranteeRange
	var store = Ext.create('Ext.data.Store', {
		model: 'PersonalInfo',
		autoLoad: true,
		//proxy: proxy
		//data: data,

/*
		proxy: {
			type: 'memory2',
			reader: {
				type: 'json',
				root: 'rows'
			}
		}
*/
/*
		proxy: {
			type: 'direct',
			directFn: QueryDatabase.getResults
		}
*/
	});

	//create the grid
	var grid = Ext.create('Ext.grid.Panel', {
		height: 450,
		width: 700,
		title: 'Velociraptor Owners',
		store: store,
		columns: [{
			dataIndex: 'ID',
			width: 50,
			text: 'ID'
		}, {
			dataIndex: 'NAME',
			flex: 1,
			text: 'Name'
		}, {
			dataIndex: 'ADDRESS',
			flex: 1.3,
			text: 'Address'
		}, {
			dataIndex: 'STATE',
			flex: 1,
			text: 'State'
		}],
		renderTo: Ext.getBody()
	});
});
