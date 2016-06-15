import java.util.ArrayList;

class RootModel {

		public int index;
		public String company;
		public String email;
		public String picture;
		public String registered;
		public String about;
		public String gender;
		public String greeting;
		public String phone;
		public String name;
		public String eyeColor;
		public String address;
		public int age;
		public String _id;
		public String balance;
		public String guid;
		public Boolean isActive;
		public ArrayList<String> tags;
		public String favoriteFruit;
		public ArrayList<FriendsModel> friends;

public RootModel(int index, String company, String email, String picture, String registered, String about, String gender, String greeting, String phone, String name, String eyeColor, String address, int age, String _id, String balance, String guid, Boolean isActive, ArrayList<String> tags, String favoriteFruit, ArrayList<FriendsModel> friends) {

		this.index = index;
		this.company = company;
		this.email = email;
		this.picture = picture;
		this.registered = registered;
		this.about = about;
		this.gender = gender;
		this.greeting = greeting;
		this.phone = phone;
		this.name = name;
		this.eyeColor = eyeColor;
		this.address = address;
		this.age = age;
		this._id = _id;
		this.balance = balance;
		this.guid = guid;
		this.isActive = isActive;
		this.tags = tags;
		this.favoriteFruit = favoriteFruit;
		this.friends = friends;

	}

}