```
//ENTITY RAP
package com.persona.Backend.Entity.Operational.GestionFormativa;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Enum.NivelRap;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;

import jakarta.persistence.Table;

@Entity
@Table(name = "rap")
public class Rap extends BaseEntity {

	@Column(name = "descripcion", length = 45, nullable = false)
	private String descripcion;

	@Column(name = "duraccion", length = 45, nullable = false)
	private Integer duraccion;

	@Column(name = "nivel", length = 45, nullable = false)
	private String nivel;

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public Integer getDuraccion() {
		return duraccion;
	}

	public void setDuraccion(Integer duraccion) {
		this.duraccion = duraccion;
	}

	public String getNivel() {
		return nivel;
	}

	public void setNivel(String nivel) {
		this.nivel = nivel;
	}
}
//IREPOSITORY RAP
package com.persona.Backend.IRepository.Operational.GestionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionFormativa.Rap;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IRapRepository extends IBaseRepository<Rap, Long>{

}
//ISERVICE RAP
package com.persona.Backend.IService.Operational.GestionFormativa;

import com.persona.Backend.Entity.Operational.GestionFormativa.Rap;
import com.persona.Backend.IService.IBaseService;

public interface IRapService extends IBaseService<Rap>{

}
//SERVICE RAP
package com.persona.Backend.Service.Operational.GestionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionFormativa.Rap;
import com.persona.Backend.IService.Operational.GestionFormativa.IRapService;
import com.persona.Backend.Service.BaseService;

@Service
public class RapService extends BaseService<Rap> implements IRapService{

}
//CONTROLLER RAP
package com.persona.Backend.Controller.Operational.GestionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionFormativa.Rap;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_formativa/rap")
public class RapController extends BaseController<Rap>{

}

```