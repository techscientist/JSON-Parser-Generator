import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;

class RootModelParser {

		FriendsModelParser friends_parser = new FriendsModelParser();

		public RootModel parseRootModel(String json_object) {

			RootModel local_model = null;
			try {
					JSONObject jsobj = new JSONObject(json_object);

					ArrayList<String> tags = new ArrayList<>();
					JSONArray tags_arr = jsobj.getJSONArray("tags");
			
					for(int i = 0 ;i<tags_arr.length()-1;i++){

 						tags.add((String)tags_arr.get(i)));

					}

					ArrayList<FriendsModel> friendss = new ArrayList<>();
					JSONArray friends_arr = jsobj.getJSONArray("friends");
			
					for(int i = 0 ;i<friends_arr.length()-1;i++){

 						friendss.add(friends_parser.parseFriendsModel((String)friends_arr.get(i)));

					}

					local_model = new RootModel(jsobj.getInt("index") , jsobj.getString("company") , jsobj.getString("email") , jsobj.getString("picture") , jsobj.getString("registered") , jsobj.getString("about") , jsobj.getString("gender") , jsobj.getString("greeting") , jsobj.getString("phone") , jsobj.getString("name") , jsobj.getString("eyeColor") , jsobj.getString("address") , jsobj.getInt("age") , jsobj.getString("_id") , jsobj.getString("balance") , jsobj.getString("guid") , jsobj.getBoolean("isActive") , tagsjsobj.getString("favoriteFruit") , friendss);
 			} 
			catch (JSONException e){

 				 e.printStackTrace();
			}

			return local_model;
		}
			
}